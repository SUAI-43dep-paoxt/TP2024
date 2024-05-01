# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QPushButton, QWidget, QVBoxLayout)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainwindow import Ui_MainWindow
from widgets.ui_authorization import Ui_Authorization
from widgets.ui_gen_invite import Ui_Invite_window
# from PyQt6.QtCore import pyqtSignal
from PySide6.QtCore import Signal, Qt, QFile
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

    def show_invite_window(self):
        self.invite_window = InviteWindow()
        self.invite_window.show()


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
