# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainwindow import Ui_MainWindow
from widgets.ui_authorization import Ui_Authorization
# from PyQt6.QtCore import pyqtSignal
from PySide6.QtCore import Signal
from invite_code.schemas import Person
from invite_code.services import *


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
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = AuthorizationDialog()
    if login_dialog.exec() == QDialog.DialogCode.Accepted:
        main_window = MainWindow()
        main_window.show()
    sys.exit(app.exec())
