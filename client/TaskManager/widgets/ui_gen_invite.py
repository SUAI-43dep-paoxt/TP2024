# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gen_invite.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Invite_window(object):
    def setupUi(self, Invite_window):
        if not Invite_window.objectName():
            Invite_window.setObjectName(u"Invite_window")
        Invite_window.resize(599, 351)
        font = QFont()
        font.setFamilies([u"Arial"])
        Invite_window.setFont(font)
        Invite_window.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(30, 30, 37);\n"
"    color: rgb(160, 160, 160);\n"
"}\n"
"QPushButton {\n"
"    background-color: white;\n"
"	color: rgb(255, 255, 255);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    padding: 35px 10px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(190, 190, 190);\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(20, 20, 26);\n"
"    border: 1px solid rgb(52, 52, 52);\n"
"	border-radius: 6px;\n"
"    padding: 7px;\n"
"}\n"
"QLineEdit::hover {\n"
"    background-color: rgb(40, 40, 48);\n"
"}")
        self.gridLayout = QGridLayout(Invite_window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame = QFrame(Invite_window)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_invite_label = QFrame(self.frame)
        self.frame_invite_label.setObjectName(u"frame_invite_label")
        self.frame_invite_label.setFrameShape(QFrame.StyledPanel)
        self.frame_invite_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_invite_label)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 15, 5, 15)
        self.label_invite_img = QLabel(self.frame_invite_label)
        self.label_invite_img.setObjectName(u"label_invite_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_invite_img.sizePolicy().hasHeightForWidth())
        self.label_invite_img.setSizePolicy(sizePolicy1)
        self.label_invite_img.setMinimumSize(QSize(0, 0))
        self.label_invite_img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_invite_img)

        self.label_invite_user = QLabel(self.frame_invite_label)
        self.label_invite_user.setObjectName(u"label_invite_user")
        self.label_invite_user.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_invite_user.setFont(font1)
        self.label_invite_user.setStyleSheet(u"")
        self.label_invite_user.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_invite_user)


        self.verticalLayout.addWidget(self.frame_invite_label, 0, Qt.AlignHCenter)

        self.lineEdit_invite_f = QLineEdit(self.frame)
        self.lineEdit_invite_f.setObjectName(u"lineEdit_invite_f")
        font2 = QFont()
        font2.setFamilies([u"Arial Rounded MT Bold"])
        font2.setPointSize(10)
        self.lineEdit_invite_f.setFont(font2)
        self.lineEdit_invite_f.setStyleSheet(u"QLineEdit::placeholder{\n"
"color: blue; \n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_invite_f)

        self.lineEdit_invite_n = QLineEdit(self.frame)
        self.lineEdit_invite_n.setObjectName(u"lineEdit_invite_n")
        self.lineEdit_invite_n.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_invite_n)

        self.lineEdit_invite_m = QLineEdit(self.frame)
        self.lineEdit_invite_m.setObjectName(u"lineEdit_invite_m")
        self.lineEdit_invite_m.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_invite_m)

        self.lineEdit_invite_email = QLineEdit(self.frame)
        self.lineEdit_invite_email.setObjectName(u"lineEdit_invite_email")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.lineEdit_invite_email.setFont(font3)
        self.lineEdit_invite_email.setStyleSheet(u"text-color: solid grey;")

        self.verticalLayout.addWidget(self.lineEdit_invite_email)

        self.frame_invite_button = QFrame(self.frame)
        self.frame_invite_button.setObjectName(u"frame_invite_button")
        self.frame_invite_button.setFrameShape(QFrame.StyledPanel)
        self.frame_invite_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_invite_button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(140, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_invite_send = QPushButton(self.frame_invite_button)
        self.pushButton_invite_send.setObjectName(u"pushButton_invite_send")
        self.pushButton_invite_send.setMinimumSize(QSize(150, 30))
        self.pushButton_invite_send.setFont(font2)
        self.pushButton_invite_send.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton_invite_send)

        self.horizontalSpacer_4 = QSpacerItem(140, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_invite_button)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.retranslateUi(Invite_window)

        QMetaObject.connectSlotsByName(Invite_window)
    # setupUi

    def retranslateUi(self, Invite_window):
        Invite_window.setWindowTitle(QCoreApplication.translate("Invite_window", u"\u0413\u0435\u043d\u0435\u0440\u0446\u0438\u044f \u043f\u0440\u0438\u0433\u043b\u0430\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u043e\u0434\u0430", None))
        self.label_invite_img.setText("")
        self.label_invite_user.setText(QCoreApplication.translate("Invite_window", u"\u041f\u0440\u0438\u0433\u043b\u0430\u0441\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.lineEdit_invite_f.setPlaceholderText(QCoreApplication.translate("Invite_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.lineEdit_invite_n.setPlaceholderText(QCoreApplication.translate("Invite_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f", None))
        self.lineEdit_invite_m.setPlaceholderText(QCoreApplication.translate("Invite_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_invite_email.setPlaceholderText(QCoreApplication.translate("Invite_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 Email", None))
        self.pushButton_invite_send.setText(QCoreApplication.translate("Invite_window", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u0434", None))
    # retranslateUi

