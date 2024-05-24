# This Python file uses the following encoding: utf-8
import sys

from datetime import datetime, timedelta
from client.TaskManager.caldav_client.schemas import Status, Task, UpdateTask
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QPushButton, QWidget, QVBoxLayout, QTreeWidgetItem)

from client.TaskManager.caldav_client.caldav_adapter import CalDavAdapter
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainwindow import Ui_MainWindow
from widgets.ui_authorization import Ui_Authorization
from widgets.ui_gen_invite import Ui_Invite_window
# from PyQt6.QtCore import pyqtSignal
from PySide6.QtCore import Signal, Qt, QFile, SIGNAL
from PySide6.QtGui import QColor
from invite_code.schemas import Person
from invite_code.services import *
from rc_resource import *



class Overlay(QWidget):
    def __init__(self, parent=None):
        super(Overlay, self).__init__(parent)
        self.setPalette(QColor(0, 0, 0, 100))
        self.setAutoFillBackground(True)


class InviteWindow(QWidget, Ui_Invite_window):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Invite_window()
        self.ui.setupUi(self)
        self.ui.pushButton_invite_send.clicked.connect(self.send_invite_code)

    def send_invite_code(self):
        print("Send")


class AuthorizationDialog(QDialog):
    login_successful = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.ui.pushButton_auth.clicked.connect(self.check_auth_data)
        self.ui.pushButton_reg.clicked.connect(self.check_reg_data)

        self.ui.pushButton_noacc_reg_up.clicked.connect(self.switch_page)
        self.ui.pushButton_haveacc_auth_up.clicked.connect(self.switch_page)

    def switch_page(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index + 1 < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(current_index + 1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def check_auth_data(self):
        # Здесь проверка учетных данных
        # Если middle name none
        person = Person(
            last_name=self.ui.lineEdit_auth_f.text(),
            first_name=self.ui.lineEdit_auth_n.text(),
            middle_name=self.ui.lineEdit_auth_m.text(),
            email=self.ui.lineEdit_auth_email.text()
        )
        try:
            invite_code = validate_invite_code(
                self.ui.lineEdit_auth_code.text(),
                person
            )
        except:
            print("Invalid invite code")


        if True:
            self.login_successful.emit()
            self.accept()

    def check_reg_data(self):
        # Здесь проверка учетных данных
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
        self.adapter = CalDavAdapter(url=URL, login=LOGIN, password=PASSWORD)
        # self.adapter.create_task(CALENDAR_NAME, test_task)
        self.filling_tree()
        self.ui.pushButton_create.clicked.connect(self.add_task)
        self.connect(self.ui.treeWidget_current, SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.onClickItem)

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
