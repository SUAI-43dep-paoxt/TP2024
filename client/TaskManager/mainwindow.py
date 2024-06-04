# This Python file uses the following encoding: utf-8
import itertools
import re
import uuid
import sys
from datetime import datetime, timedelta
from string import printable

import pyperclip
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal, QDate, QTimer
from PySide6.QtGui import QColor, QPalette, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QWidget, QTreeWidgetItem)
from _queue import Empty
from plyer import notification

from caldav_client.caldav_adapter import CalDavAdapter
from caldav_client.notifications.notification_worker import run_notification_worker
from caldav_client.schemas import CalDavInfo, Status, Task, UpdateTask
from image_generation.img_generator import GenerateAvatar
from invite_code.services import *
from session import SessionStorage
from ui_mainwindow import Ui_MainWindow
from widgets.ui_acceptionWin import Ui_AcceptionWin
from widgets.ui_authorization import Ui_Authorization
from widgets.ui_gen_invite import Ui_Invite_window
from widgets.ui_warningWin import Ui_WarningWin

DEBUG = False
DEBUG_CALDAV_CONNECTION = CalDavInfo(
    username='admin',
    password='admin',
    url='http://localhost:80/remote.php/dav',
    calendar_name="Задачи"
)


def validate_name(name):
    """ Проверка, что введенные значения состоят только из букв и пробелов """
    return re.match(r"^[A-Za-zА-Яа-я\s]+$", name) is not None


def validate_email(email):
    """ Проверка адреса электронной почты """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


def show_error_window(err_win_title, err_text):
    dialog = WarningWin(err_win_title, err_text)
    dialog.show()
    if dialog.exec():
        pass
    raise ValidationError(err_text)


def validate_base_input(last_name, first_name, middle_name, email):
    """ Функция проверки базовых данных на корректность: ФИО, адрес почты """

    if validate_name(last_name) and validate_name(first_name):
        print("Фамилия и имя верны")
        if middle_name:
            # Если отчество было введено, проверяем его
            if validate_name(middle_name):
                print("Отчество верно")
            else:
                show_error_window("Ошибка", "Некорректное отчество")

    else:
        show_error_window("Ошибка", "Некорректные фамилия или имя")

    if validate_email(email):
        print("Адрес электронной почты верный")
    else:
        show_error_window("Ошибка", "Некорректный адрес почты")

    def validate_create_input(self, url_nc, calendar_name, pswrd):
        """ Функция проверки данных для создания проекта на корректность: url NC, имя проекта, пароль """
        pass


class DialogAcception(QDialog, Ui_AcceptionWin):
    """ Класс окна с кнопками подтверждения """

    def __init__(self, attention_win_title, attention_text):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(attention_win_title)
        self.label_description.setText(attention_text)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Подтвердить")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Отмена")


class WarningWin(QDialog, Ui_WarningWin):
    """ Класс диалогового окна с одной кнопкой """

    def __init__(self, error_win_title, error_text, label_text=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(error_win_title)
        self.label_description.setText(error_text)
        self.pushButton_ok.clicked.connect(lambda: self.close())
        if label_text:
            self.label_warning.setText("Внимание")


class ValidationError(Exception):
    """ Класс ошибки валидации данных"""

    def __init__(self, message="Ошибка ввода данных"):
        self.message = message
        super().__init__(self.message)


class InviteWindow(QWidget, Ui_Invite_window):
    def __init__(self, adapter: CalDavAdapter, project_name: str):
        super().__init__()
        self.ui = Ui_Invite_window()
        self.ui.setupUi(self)
        self.ui.pushButton_invite_send.clicked.connect(self.send_invite_code)

        # Изменение цветов placeholder для QLineEdit
        self.line_edit_list = [self.ui.lineEdit_invite_f,
                               self.ui.lineEdit_invite_n,
                               self.ui.lineEdit_invite_m,
                               self.ui.lineEdit_invite_email]
        palette = self.line_edit_list[0].palette()
        palette.setColor(QPalette.PlaceholderText, QColor(161, 161, 170))
        self.adapter = adapter
        self.project_name = project_name
        for line_edit in self.line_edit_list:
            line_edit.setPalette(palette)

    def send_invite_code(self):
        # Здесь данные должны грузиться из session storage и генерируется инвайт-код
        # не работает с кириллицей
        line_edit_list_texts = [self.ui.lineEdit_invite_f.text(),
                                self.ui.lineEdit_invite_n.text(),
                                self.ui.lineEdit_invite_m.text(),
                                self.ui.lineEdit_invite_email.text()]
        try:
            validate_base_input(line_edit_list_texts[0],
                                line_edit_list_texts[1],
                                line_edit_list_texts[2],
                                line_edit_list_texts[3])

            invite_code = InviteCode(person=Person(last_name=line_edit_list_texts[0],
                                                   first_name=line_edit_list_texts[1],
                                                   middle_name=line_edit_list_texts[2],
                                                   email=line_edit_list_texts[3],
                                                   ),
                                     caldav_info=CalDavInfo(username=self.adapter.login,
                                                            password=self.adapter.password,
                                                            url=self.adapter.url,
                                                            calendar_name=self.adapter.calendar_name,
                                                            ),
                                     project_name=self.project_name)

            text = get_encrypted_invite_code(invite_code)
            pyperclip.copy(text)
            show_error_window("Инвайт-код был создан", "Инвайт-код сохранён в буфер обмена")

        except ValidationError as e:
            print(f"Обработано исключение: {e}")
        except:
            print("Ошибка создания инвайт-кода")


class AuthorizationDialog(QDialog):
    login_successful = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.ui.pushButton_auth.clicked.connect(self.check_auth_data)
        self.ui.pushButton_reg.clicked.connect(self.check_reg_data)

        self.ui.pushButton_noacc_reg_up.clicked.connect(self.switch_page)
        self.ui.pushButton_noacc_reg.clicked.connect(self.switch_page)

        self.ui.pushButton_haveacc_auth_up.clicked.connect(self.switch_page)
        self.ui.pushButton_haveacc_auth.clicked.connect(self.switch_page)

        self.dict_calendar_empty_lineedits = {}
        self.dict_calendar_empty_labels = {}
        self.session_storage = SessionStorage()

    def generate_avatar(self, n, m, f):
        image = GenerateAvatar(n,
                               m,
                               f)

        if DEBUG:
            self.ui.lineEdit_reg_password.setText(DEBUG_CALDAV_CONNECTION.password)
            self.ui.lineEdit_reg_project_name.setText(DEBUG_CALDAV_CONNECTION.calendar_name)
            self.ui.lineEdit_reg_url_nc.setText(DEBUG_CALDAV_CONNECTION.url)
            self.ui.lineEdit_reg_username.setText(DEBUG_CALDAV_CONNECTION.username)

    def switch_page(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index + 1 < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(current_index + 1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def check_auth_data(self):
        last_name = self.ui.lineEdit_auth_f.text()
        first_name = self.ui.lineEdit_auth_n.text()
        middle_name = self.ui.lineEdit_auth_m.text()
        email = self.ui.lineEdit_auth_email.text()

        try:
            validate_base_input(last_name, first_name, middle_name, email)

            if self.ui.lineEdit_auth_code.text() == "":
                show_error_window("Ошибка", "Поле с пригласительным кодом обязательно")

            person = Person(
                last_name=self.ui.lineEdit_auth_f.text(),
                first_name=self.ui.lineEdit_auth_n.text(),
                middle_name=self.ui.lineEdit_auth_m.text(),
                email=self.ui.lineEdit_auth_email.text()
            )
            invite_code = validate_invite_code(
                self.ui.lineEdit_auth_code.text(),
                person
            )
            self.session_storage.add(invite_code)
        except ValidationError as e:
            print(f"Обработано исключение: {e}")
        except Exception as e:
            print(e)
            print("Invalid invite code")

        self.generate_avatar(last_name, first_name, middle_name)
        self.login_successful.emit()
        self.accept()

    def check_reg_data(self):
        last_name = self.ui.lineEdit_reg_f.text()
        first_name = self.ui.lineEdit_reg_n.text()
        middle_name = self.ui.lineEdit_reg_m.text()
        email = self.ui.lineEdit_reg_email.text()

        self.dict_calendar_empty_lineedits["calendar_name"] = [self.ui.lineEdit_reg_project_name.text(),
                                                               self.ui.label_reg_project_name.text()]
        self.dict_calendar_empty_lineedits["url_nc"] = [self.ui.lineEdit_reg_url_nc.text(),
                                                        self.ui.label_reg_url.text()]
        self.dict_calendar_empty_lineedits["username"] = [self.ui.lineEdit_reg_password.text(),
                                                          self.ui.label_reg_password.text()]  # логин CalDAV
        self.dict_calendar_empty_lineedits["password"] = [self.ui.lineEdit_reg_username.text(),
                                                          self.ui.label_reg_username.text()]

        try:
            validate_base_input(last_name, first_name, middle_name, email)
            # проверка введённых данных календаря
            empty_keys = [v[1] for v in self.dict_calendar_empty_lineedits.values() if not v[0]]

            if empty_keys:
                show_error_window("Ошибка", f"Следующие поля не заполнены: {', '.join(empty_keys)}")

            person = Person(
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                email=email
            )

            invite_code = InviteCode(
                project_name=self.ui.lineEdit_reg_project_name.text(),
                person=person,
                caldav_info=CalDavInfo(
                    username=self.ui.lineEdit_reg_username.text(),
                    password=self.ui.lineEdit_reg_password.text(),
                    url=self.ui.lineEdit_reg_url_nc.text(),
                    calendar_name="",
                )
            )

            calendar_name = "".join(filter(lambda c: c in printable, invite_code.project_name)) + f"-{uuid.uuid4().hex}"

            try:
                CalDavAdapter.create_calendar(
                    url=invite_code.caldav_info.url,
                    login=invite_code.caldav_info.username,
                    password=invite_code.caldav_info.password,
                    name=calendar_name,
                )
            except Exception as e:
                show_error_window("Ошибка", "Некорректные данные CalDAV")
                print(e)
                return

            invite_code.caldav_info.calendar_name = calendar_name
            self.session_storage.add(invite_code)
            self.generate_avatar(last_name, first_name, middle_name)
            self.login_successful.emit()
            self.accept()

        except ValidationError as e:
            print(f"Обработано исключение: {e}")
        except:
            show_error_window("Ошибка", f"Ошибка создания календаря")


class MainWindow(QMainWindow):
    def __init__(self, project_name: str, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.popup.setDateTime(datetime.now())
        self.uid = {}
        self.set_uid = ''

        # ---- Аватар -----
        # self.ui.account_button.setIcon(
        #    QIcon("images\\avatar.png"))
        # self.ui.account_button.setStyleSheet("""
        # QPushButton{
        #     max-width: 28px;
        #     max-height: 28px;
        # }
        # """)
        # ---- Аватар -----

        # Вызов инвайт-формы
        self.ui.invite_button.clicked.connect(self.show_invite_window)
        self.widget = None
        self.session_storage = SessionStorage()
        self.current_session = self.session_storage.sessions[project_name]
        self.adapter = CalDavAdapter(
            url=self.current_session.caldav_info.url,
            login=self.current_session.caldav_info.username,
            password=self.current_session.caldav_info.password,
            calendar_name=self.current_session.caldav_info.calendar_name,
        )

        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.invite_button.clicked.connect(lambda:
                                              self.set_visible_input_panel(True))

        self.filling_tree()
        self.ui.pushButton_add_task.clicked.connect(self.add_task)
        self.ui.treeWidget_current.itemClicked.connect(self.onItemClicked)  #
        self.ui.treeWidget_overdue.itemClicked.connect(self.onItemClicked)  #
        self.ui.treeWidget_completed.itemClicked.connect(self.onItemClicked)  # ###################
        self.ui.pushButton_create.clicked.connect(lambda:
                                                  self.set_visible_input_panel(True))

        self.ui.pushButton_delete_task.clicked.connect(self.delete_task)

        self.timer = QTimer(self)
        self.queue = run_notification_worker(
            caldav_adapters=[self.adapter],
            executor=self.current_session.person.email,
        )

        self.start_handling_notifications()

        self.status_to_index_value = {
            Status.todo: 0,
            Status.in_progress: 1,
            Status.done: 2,
        }

        self.index_value_to_status = {
            0: Status.todo,
            1: Status.in_progress,
            2: Status.done,
        }

    def start_handling_notifications(self):
        self.timer.timeout.connect(self.handle_notifications)
        self.timer.start(1000)

    def handle_notifications(self):
        try:
            while item := self.queue.get_nowait():
                notification.notify(
                    title="Наступает дедлайн по задаче",
                    message=f"Скоро нужно завершить «{item.title}»",
                    app_name="TP2024",
                )
        except Empty:
            return

    def set_visible_input_panel(self, visible=True):
        if visible:
            self.ui.pushButton_add_task.setText('Добавить задачу')
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.taska.setText(self.ui.lineEdit_add_task.text())
        self.ui.pushButton_delete_task.setVisible(False)

    def delete_task(self):
        self.adapter.delete_task(uid=self.set_uid)
        self.filling_tree()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.clear_task()

    def clear_task(self):
        self.ui.taska.clear()
        self.ui.lineEdit_task_description.clear()

    def add_task(self):
        """
        Метод добавления задачи в NextCloud.

        Получает данные из виджетов интерфейса (название задачи, описание,
        дату завершения и теги), создает объект задачи Task и добавляет его в
        NextCloud календарь.

        В случае не заполнения всех необходимых виджетов,
        выводит сообщение об ошибке.
        """
        end_time = datetime.strptime(self.ui.popup.text().replace('.', '-') + " 23:59:59",
                                     '%d-%m-%Y %H:%M:%S')
        print(f"{self.current_session.person.email=}")
        task = Task(
            title=self.ui.taska.text(),
            description=self.ui.lineEdit_task_description.text(),
            start_time=datetime(2000, 1, 1),
            end_time=end_time,
            status=self.index_value_to_status[self.ui.comboBox_status.currentIndex()],
            tags=self.ui.lineEdit_tags.text().split(),
            creator=self.current_session.person.email,
            executor=self.ui.comboBox.currentText(),
        )
        if self.ui.pushButton_add_task.text() == 'Добавить задачу':
            self.adapter.create_task(task)
            self.ui.lineEdit_add_task.clear()
            self.set_visible_input_panel(False)
        else:
            self.adapter.update_task(self.set_uid, task)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.filling_tree()

    def filling_tree(self):
        """
        Метод заполнения центральной панели задачами из NextCloud.

        Заполняет центральную панель виджетами задач на текущую неделю из NextCloud.
        Извлекает все задачи на текущую неделю, разделяет их по дням недели и
        отображает в соответствующих разделах 'Просроченные задачи' и
        'Текущие задачи'.
        """

        # Дни недели для заполнения деревьев
        WEEKDAY = [
            'Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота',
            'Воскресенье'
        ]

        # Вычисление начала недели
        start = datetime.now() - timedelta(days=datetime.now().weekday()) - timedelta(days=1)
        # Вычисление конца недели
        end = start + timedelta(days=6)

        # 'Вытягивание' всех задач на текущую неделю
        tasks = self.adapter.get_tasks(from_date=start,
                                       to_date=end)

        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(sorted(set(itertools.chain(*[(task.executor, task.creator) for task in tasks]))))

        tags = sorted(set(itertools.chain(*[task.tags for task in tasks])))
        self.ui.treeWidget.clear()
        for tag in tags:
            if not tag.strip():
                continue
            tag_tree = QTreeWidgetItem(self.ui.treeWidget)
            tag_tree.setText(0, tag)

        # Текущий день недели
        current_week_day = datetime.now().weekday()

        # Ссылки на виджеты в 'Просроченные задачи'
        overdue_days = []
        self.ui.treeWidget_overdue.clear()
        for day in range(0, current_week_day):
            root = QTreeWidgetItem(self.ui.treeWidget_overdue)
            root.setText(0, WEEKDAY[day])
            overdue_days.append(root)

        # Ссылки на виджеты в 'Выполнены'
        completed_days = []
        self.ui.treeWidget_completed.clear()
        for day in range(current_week_day - 7, current_week_day):
            root = QTreeWidgetItem(self.ui.treeWidget_completed)
            root.setText(0, WEEKDAY[day])
            completed_days.append(root)

        # Ссылки на виджеты в 'Текущие задачи'
        current_days = []
        self.ui.treeWidget_current.clear()
        for day in range(current_week_day, 7):
            root = QTreeWidgetItem(self.ui.treeWidget_current)
            root.setText(0, WEEKDAY[day])
            current_days.append(root)

        current_count = 0
        overdue_count = 0
        completed_count = 0
        for task in tasks:
            end_time_task = task.end_time.weekday()  # Дедлайн задачи

            print(task.status, task.status == Status.done)
            if task.status == Status.done:
                self.show_task(task, completed_days[end_time_task])
                completed_count += 1
                continue

            if current_week_day <= end_time_task:  # Проверка задачи (текущий день <= дедлайна)
                self.show_task(task,
                                current_days[end_time_task - current_week_day])
                overdue_count += 1

            else:
                self.show_task(task,
                                overdue_days[end_time_task])
                current_count += 1

        self.ui.toolBox.setItemText(0, f'Просрочено, {current_count}')
        self.ui.toolBox.setItemText(1, f'Текущие, {overdue_count}')
        self.ui.toolBox.setItemText(2, f'Выполнено, {completed_count}')

    def onItemClicked(self, it, col):
        try:
            task_uid = self.uid[str(it)]
            task = self.adapter.get_task(task_uid)

            self.set_visible_input_panel()
            self.ui.taska.setText(it.text(col))
            self.ui.lineEdit_tags.setText(" ".join(task.tags))
            self.ui.lineEdit_task_description.setText(it.child(0).text(col))
            self.ui.pushButton_add_task.setText('Изменить')
            self.ui.pushButton_delete_task.setVisible(True)
            self.set_uid = task_uid

            self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findText(task.executor))

            self.ui.comboBox_status.setCurrentIndex(self.status_to_index_value[task.status])
            # self.adapter.update_task(self.uid[str(it)], UpdateTask(status=Status.done))
            # print(self.adapter.get_task(self.uid[str(it)]))
        except Exception as e:
            print(e)

    def show_task(self, task, root_tree) -> None:
        """
        Вывод задачи на экран в виджет QTreeWidgetItem

        Параметры:
            task: Task
                Объект задачи, содержащий информацию о названии,
                описании и тегах задачи.
            root_tree: QTreeWidgetItem
                Родительский виджет QTreeWidgetItem, в который будет
                добавлена информация о задаче.

        Выводит информацию о задаче на экран в виджет QTreeWidgetItem.
        Создает дочерние виджеты для отображения названия задачи, ее описания и тегов.

        """
        # Добавление виджета с названием задачи (title)
        task_tree = QTreeWidgetItem(root_tree)
        task_tree.setText(0, task.title)
        self.uid[str(task_tree)] = task.uid
        # Добавление виджета с описанием задачи (description)
        description = QTreeWidgetItem(task_tree)
        description.setText(0, task.description)
        # Добавление виджета с тегами задачи (tags)
        for i, tag in enumerate(task.tags):
            tags = QTreeWidgetItem(task_tree)
            tags.setText(0, tag)

    def show_invite_window(self):
        self.invite_window = InviteWindow(self.adapter, self.current_session.project_name)
        self.invite_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_file = "styles/styles.qss"
    with open(style_file, "r", encoding='UTF-8') as f:
        app.setStyleSheet(f.read())

    session_storage = SessionStorage()

    login_dialog = None

    if not session_storage.sessions:
        login_dialog = AuthorizationDialog()

    if session_storage.sessions or login_dialog.exec() == QDialog.DialogCode.Accepted:
        first_session = session_storage.sessions[list(session_storage.sessions.keys())[0]]
        main_window = MainWindow(project_name=first_session.project_name)
        main_window.show()
    sys.exit(app.exec())
