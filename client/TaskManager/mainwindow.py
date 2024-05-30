# This Python file uses the following encoding: utf-8
import re
import sys
import pyperclip

from datetime import datetime, timedelta
from PySide6 import QtGui, QtWidgets
from TP2024.client.TaskManager.caldav_client.schemas import Status, Task, UpdateTask
from TP2024.client.TaskManager.caldav_client.caldav_adapter import CalDavAdapter
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QPushButton, QWidget, QVBoxLayout, QTreeWidgetItem, QLineEdit)
from ui_mainwindow import Ui_MainWindow
from widgets.ui_warningWin import Ui_WarningWin
from widgets.ui_acceptionWin import Ui_AcceptionWin
from widgets.ui_authorization import Ui_Authorization
from widgets.ui_gen_invite import Ui_Invite_window
from PySide6.QtCore import Signal, Qt, QFile, SIGNAL
from PySide6.QtGui import QColor, QPalette
from invite_code.schemas import Person
from invite_code.services import *
from rc_resource import *
from caldav_client.schemas import CalDavInfo


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
    def __init__(self):
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
                                     caldav_info=CalDavInfo(username="test1",
                                                            password="test2",
                                                            url="test_url",
                                                            calendar_name="test_cal_name",
                                                            ), project_name="......")

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

        self.dict_calendar_info = {}

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
        except ValidationError as e:
            print(f"Обработано исключение: {e}")
        except:
            print("Invalid invite code")

        if True:
            self.login_successful.emit()
            self.accept()

    def check_reg_data(self):
        last_name = self.ui.lineEdit_reg_f.text()
        first_name = self.ui.lineEdit_reg_n.text()
        middle_name = self.ui.lineEdit_reg_m.text()
        email = self.ui.lineEdit_reg_email.text()

        self.dict_calendar_info["calendar_name"] = self.ui.lineEdit_reg_calendar_name.text()
        self.dict_calendar_info["url_nc"] = self.ui.lineEdit_reg_url_nc.text()
        self.dict_calendar_info["username"] = self.ui.lineEdit_reg_password.text()  # логин CalDAV
        self.dict_calendar_info["password"] = self.ui.lineEdit_reg_username.text()

        # код из авторизации - изменить логику для регистрации
        try:
            validate_base_input(last_name, first_name, middle_name, email)

            empty_keys = [k for k, v in self.dict_calendar_info.items() if not v]
            if empty_keys:
                show_error_window("Ошибка", f"Следующие поля не заполнены: {', '.join(empty_keys)}")

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
        except ValidationError as e:
            print(f"Обработано исключение: {e}")
        except:
            print("Invalid invite code")

        if True:
            self.login_successful.emit()
            self.accept()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Вызов инвайт-формы
        self.ui.invite_button.clicked.connect(self.show_invite_window)
        self.widget = None

        '''
        Подключение к NextCloud 
        URL = 'http://localhost:8080/remote.php/dav'
        LOGIN = 'admin'
        PASSWORD = 'admin'
        CALENDAR_NAME = 'abs'
        '''
        # test_task = Task(
        #     title='Задание №7',
        #     description='Описание',
        #     start_time=datetime.now() - timedelta(days=3),
        #     end_time=datetime.now() - timedelta(days=2),
        #     status=Status.in_progress,
        #     tags=['qwe', 'rty'],
        # )

        # ----! DELETE COMMENTS FOR\BEFORE USING !------
        # ЧТОБЫ ЗАПУСТИТЬ ПРИЛОЖЕНИЕ В ТЕСТОВОМ РЕЖИМЕ БЕЗ NC - НУЖНО ЗАККОМЕНТИРОВАТЬ КОД НИЖЕ

        # self.adapter = CalDavAdapter(url=URL, login=LOGIN, password=PASSWORD)
        # # self.adapter.create_task(CALENDAR_NAME, test_task)
        # self.filling_tree()
        # self.ui.pushButton_create.clicked.connect(self.add_task)
        # self.connect(self.ui.treeWidget_current, SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.onClickItem)


    def show_invite_window(self):
        self.invite_window = InviteWindow()
        self.invite_window.show()

    def add_task(self):
        """
        Метод добавления задачи в NextCloud
        """
        end_time = datetime.strptime(self.ui.calendarWidget.selectedDate().toString('dd-MM-yyyy'),
                                     '%d-%m-%Y')
        try:
            test_task = Task(
                title=self.ui.lineEdit_add_task.text(),
                description=self.ui.lineEdit_task_description.text(),
                start_time=datetime.now(),
                end_time=end_time,
                status=Status.in_progress,
                tags=['qwe', 'rty'],
            )
            self.adapter.create_task(CALENDAR_NAME, test_task)
        except:
            print('Виджеты не заполнены!')

    def filling_tree(self):
        """Заполненяет центральную панель задачами из NextCloud"""

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
        start = datetime.now() - timedelta(days=datetime.now().weekday())
        # Вычисление конца недели
        end = start + timedelta(days=6)

        # 'Вытягивание' всех задач на текущую неделю
        tasks = self.adapter.get_tasks(CALENDAR_NAME,
                                       from_date=start,
                                       to_date=end)

        # Текущий день недели
        current_week_day = datetime.now().weekday()

        # Ссылки на виджеты в 'Просроченные задачи'
        overdue_days = []
        self.ui.treeWidget_overdue.clear()
        for day in range(0, current_week_day):
            root = QTreeWidgetItem(self.ui.treeWidget_overdue)
            root.setText(0, WEEKDAY[day])
            overdue_days.append(root)

        # Ссылки на виджеты в 'Текущие задачи'
        current_days = []
        self.ui.treeWidget_current.clear()
        for day in range(current_week_day, 7):
            root = QTreeWidgetItem(self.ui.treeWidget_current)
            root.setText(0, WEEKDAY[day])
            current_days.append(root)

        for task in tasks:
            end_time_task = task.end_time.weekday()  # Дедлайн задачи
            if current_week_day <= end_time_task:  # Проверка задачи (текущий день < дедлайна)
                if task.status == Status.todo:  # Проверка задачи (статус задачи == 'TO DO')
                    self.show_task(task,
                                   current_days[current_week_day - end_time_task])

            else:
                if task.status == Status.in_progress:  # Проверка задачи (статус задачи == 'IN PROGRESS')
                    self.show_task(task,
                                   overdue_days[end_time_task])

    def show_task(self, task, root_tree) -> None:
        """
        Вывод задачи на экран в виджет QTreeWidgetItem

        """
        # Додавление виджета с названием задачи (title)
        task_tree = QTreeWidgetItem(root_tree)
        task_tree.setText(0, task.title)
        # Додавление виджета с описанием задачи (description)
        description = QTreeWidgetItem(task_tree)
        description.setText(0, task.description)
        # Додавление виджета с тегами задачи (tags)
        tags = QTreeWidgetItem(task_tree)
        tags.setText(0, task.tags[0])

    def onClickItem(self, item, column):
        print(item, column)

    def show_invite_window(self):
        self.invite_window = InviteWindow()
        self.invite_window.show()


# testdata
URL = 'http://localhost:8080/remote.php/dav'
LOGIN = 'admin'
PASSWORD = 'admin'
CALENDAR_NAME = 'abs'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_file = "styles/styles.qss"
    with open(style_file, "r", encoding='UTF-8') as f:
        app.setStyleSheet(f.read())
    login_dialog = AuthorizationDialog()
    if login_dialog.exec() == QDialog.DialogCode.Accepted:
        main_window = MainWindow()
        main_window.show()
    sys.exit(app.exec())
