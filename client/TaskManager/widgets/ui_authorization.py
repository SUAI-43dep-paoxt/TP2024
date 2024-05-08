# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        if not Authorization.objectName():
            Authorization.setObjectName(u"Authorization")
        Authorization.resize(1334, 800)
        self.horizontalLayout = QHBoxLayout(Authorization)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.black_info = QFrame(Authorization)
        self.black_info.setObjectName(u"black_info")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.black_info.sizePolicy().hasHeightForWidth())
        self.black_info.setSizePolicy(sizePolicy)
        self.black_info.setStyleSheet(u"QWidget{\n"
"background-color: #18181B;\n"
"color: white;\n"
"}")
        self.black_info.setFrameShape(QFrame.StyledPanel)
        self.black_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.black_info)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 30, 50, 30)
        self.frame_3 = QFrame(self.black_info)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border: 0px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_app_img = QLabel(self.frame_3)
        self.label_app_img.setObjectName(u"label_app_img")

        self.horizontalLayout_2.addWidget(self.label_app_img)

        self.label_app_name = QLabel(self.frame_3)
        self.label_app_name.setObjectName(u"label_app_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_app_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_app_name, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.verticalSpacer_7 = QSpacerItem(20, 653, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.label_app_quote = QLabel(self.black_info)
        self.label_app_quote.setObjectName(u"label_app_quote")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_app_quote.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_app_quote)

        self.label_app_author_quote = QLabel(self.black_info)
        self.label_app_author_quote.setObjectName(u"label_app_author_quote")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_app_author_quote.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_app_author_quote)


        self.horizontalLayout.addWidget(self.black_info)

        self.stackedWidget = QStackedWidget(Authorization)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.registration_page = QWidget()
        self.registration_page.setObjectName(u"registration_page")
        self.horizontalLayout_4 = QHBoxLayout(self.registration_page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_reg_grid = QFrame(self.registration_page)
        self.frame_reg_grid.setObjectName(u"frame_reg_grid")
        sizePolicy.setHeightForWidth(self.frame_reg_grid.sizePolicy().hasHeightForWidth())
        self.frame_reg_grid.setSizePolicy(sizePolicy)
        self.frame_reg_grid.setStyleSheet(u"QFrame{\n"
"border: 0px;\n"
"color:black;\n"
"}")
        self.frame_reg_grid.setFrameShape(QFrame.StyledPanel)
        self.frame_reg_grid.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_reg_grid)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(50, 30, 50, 30)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 2)

        self.frame_reg_main = QFrame(self.frame_reg_grid)
        self.frame_reg_main.setObjectName(u"frame_reg_main")
        self.frame_reg_main.setFrameShape(QFrame.StyledPanel)
        self.frame_reg_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_reg_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_reg_main = QLabel(self.frame_reg_main)
        self.label_reg_main.setObjectName(u"label_reg_main")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_reg_main.setFont(font3)
        self.label_reg_main.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_reg_main)

        self.verticalSpacer_3 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_reg_email = QLabel(self.frame_reg_main)
        self.label_reg_email.setObjectName(u"label_reg_email")

        self.verticalLayout.addWidget(self.label_reg_email)

        self.lineEdit_reg_email = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_email.setObjectName(u"lineEdit_reg_email")

        self.verticalLayout.addWidget(self.lineEdit_reg_email)

        self.label_reg_f = QLabel(self.frame_reg_main)
        self.label_reg_f.setObjectName(u"label_reg_f")

        self.verticalLayout.addWidget(self.label_reg_f)

        self.lineEdit_reg_f = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_f.setObjectName(u"lineEdit_reg_f")

        self.verticalLayout.addWidget(self.lineEdit_reg_f)

        self.label_reg_n = QLabel(self.frame_reg_main)
        self.label_reg_n.setObjectName(u"label_reg_n")

        self.verticalLayout.addWidget(self.label_reg_n)

        self.lineEdit_reg_n = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_n.setObjectName(u"lineEdit_reg_n")

        self.verticalLayout.addWidget(self.lineEdit_reg_n)

        self.label_reg_m = QLabel(self.frame_reg_main)
        self.label_reg_m.setObjectName(u"label_reg_m")

        self.verticalLayout.addWidget(self.label_reg_m)

        self.lineEdit_reg_m = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_m.setObjectName(u"lineEdit_reg_m")

        self.verticalLayout.addWidget(self.lineEdit_reg_m)

        self.label_reg_url = QLabel(self.frame_reg_main)
        self.label_reg_url.setObjectName(u"label_reg_url")

        self.verticalLayout.addWidget(self.label_reg_url)

        self.lineEdit_reg_url_nc = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_url_nc.setObjectName(u"lineEdit_reg_url_nc")

        self.verticalLayout.addWidget(self.lineEdit_reg_url_nc)

        self.label_reg_calendar_name = QLabel(self.frame_reg_main)
        self.label_reg_calendar_name.setObjectName(u"label_reg_calendar_name")

        self.verticalLayout.addWidget(self.label_reg_calendar_name)

        self.lineEdit_reg_calendar_name = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_calendar_name.setObjectName(u"lineEdit_reg_calendar_name")

        self.verticalLayout.addWidget(self.lineEdit_reg_calendar_name)

        self.label_reg_password1 = QLabel(self.frame_reg_main)
        self.label_reg_password1.setObjectName(u"label_reg_password1")

        self.verticalLayout.addWidget(self.label_reg_password1)

        self.lineEdit_reg_password1 = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_password1.setObjectName(u"lineEdit_reg_password1")

        self.verticalLayout.addWidget(self.lineEdit_reg_password1)

        self.label_reg_password2 = QLabel(self.frame_reg_main)
        self.label_reg_password2.setObjectName(u"label_reg_password2")

        self.verticalLayout.addWidget(self.label_reg_password2)

        self.lineEdit_reg_password2 = QLineEdit(self.frame_reg_main)
        self.lineEdit_reg_password2.setObjectName(u"lineEdit_reg_password2")

        self.verticalLayout.addWidget(self.lineEdit_reg_password2)

        self.frame_haveacc_auth = QFrame(self.frame_reg_main)
        self.frame_haveacc_auth.setObjectName(u"frame_haveacc_auth")
        self.frame_haveacc_auth.setFrameShape(QFrame.StyledPanel)
        self.frame_haveacc_auth.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_haveacc_auth)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_haveacc = QLabel(self.frame_haveacc_auth)
        self.label_haveacc.setObjectName(u"label_haveacc")

        self.horizontalLayout_5.addWidget(self.label_haveacc)

        self.pushButton_haveacc_auth = QPushButton(self.frame_haveacc_auth)
        self.pushButton_haveacc_auth.setObjectName(u"pushButton_haveacc_auth")
        self.pushButton_haveacc_auth.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	color:blue;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-decoration: underline;\n"
"	color:blue;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_haveacc_auth)


        self.verticalLayout.addWidget(self.frame_haveacc_auth, 0, Qt.AlignHCenter)

        self.pushButton_reg = QPushButton(self.frame_reg_main)
        self.pushButton_reg.setObjectName(u"pushButton_reg")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.pushButton_reg.setFont(font4)
        self.pushButton_reg.setStyleSheet(u"QWidget{\n"
"background-color: #18181B;\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_reg)


        self.gridLayout.addWidget(self.frame_reg_main, 2, 1, 2, 2)

        self.frame_haveacc_auth_up = QFrame(self.frame_reg_grid)
        self.frame_haveacc_auth_up.setObjectName(u"frame_haveacc_auth_up")
        self.frame_haveacc_auth_up.setFrameShape(QFrame.StyledPanel)
        self.frame_haveacc_auth_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_haveacc_auth_up)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, -1, -1, -1)
        self.pushButton_haveacc_auth_up = QPushButton(self.frame_haveacc_auth_up)
        self.pushButton_haveacc_auth_up.setObjectName(u"pushButton_haveacc_auth_up")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        self.pushButton_haveacc_auth_up.setFont(font5)
        self.pushButton_haveacc_auth_up.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	color:black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-decoration: underline;\n"
"	color:black;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_haveacc_auth_up, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_haveacc_auth_up, 0, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 2, 1)


        self.horizontalLayout_4.addWidget(self.frame_reg_grid)

        self.stackedWidget.addWidget(self.registration_page)
        self.authorization_page = QWidget()
        self.authorization_page.setObjectName(u"authorization_page")
        self.horizontalLayout_8 = QHBoxLayout(self.authorization_page)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_auth_grid = QFrame(self.authorization_page)
        self.frame_auth_grid.setObjectName(u"frame_auth_grid")
        self.frame_auth_grid.setStyleSheet(u"QFrame{\n"
"border: 0px;\n"
"color:black;\n"
"}")
        self.frame_auth_grid.setFrameShape(QFrame.StyledPanel)
        self.frame_auth_grid.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_auth_grid)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(50, 30, 50, 30)
        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.auth_frame_main = QFrame(self.frame_auth_grid)
        self.auth_frame_main.setObjectName(u"auth_frame_main")
        self.auth_frame_main.setFrameShape(QFrame.StyledPanel)
        self.auth_frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.auth_frame_main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_auth_login = QLabel(self.auth_frame_main)
        self.label_auth_login.setObjectName(u"label_auth_login")
        self.label_auth_login.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_auth_login, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.label_auth_f = QLabel(self.auth_frame_main)
        self.label_auth_f.setObjectName(u"label_auth_f")

        self.verticalLayout_3.addWidget(self.label_auth_f)

        self.lineEdit_auth_f = QLineEdit(self.auth_frame_main)
        self.lineEdit_auth_f.setObjectName(u"lineEdit_auth_f")

        self.verticalLayout_3.addWidget(self.lineEdit_auth_f)

        self.label_auth_n = QLabel(self.auth_frame_main)
        self.label_auth_n.setObjectName(u"label_auth_n")

        self.verticalLayout_3.addWidget(self.label_auth_n)

        self.lineEdit_auth_n = QLineEdit(self.auth_frame_main)
        self.lineEdit_auth_n.setObjectName(u"lineEdit_auth_n")

        self.verticalLayout_3.addWidget(self.lineEdit_auth_n)

        self.label_auth_m = QLabel(self.auth_frame_main)
        self.label_auth_m.setObjectName(u"label_auth_m")

        self.verticalLayout_3.addWidget(self.label_auth_m)

        self.lineEdit_auth_m = QLineEdit(self.auth_frame_main)
        self.lineEdit_auth_m.setObjectName(u"lineEdit_auth_m")

        self.verticalLayout_3.addWidget(self.lineEdit_auth_m)

        self.label_auth_email = QLabel(self.auth_frame_main)
        self.label_auth_email.setObjectName(u"label_auth_email")

        self.verticalLayout_3.addWidget(self.label_auth_email)

        self.lineEdit_auth_email = QLineEdit(self.auth_frame_main)
        self.lineEdit_auth_email.setObjectName(u"lineEdit_auth_email")

        self.verticalLayout_3.addWidget(self.lineEdit_auth_email)

        self.label_auth_code = QLabel(self.auth_frame_main)
        self.label_auth_code.setObjectName(u"label_auth_code")

        self.verticalLayout_3.addWidget(self.label_auth_code)

        self.lineEdit_auth_code = QLineEdit(self.auth_frame_main)
        self.lineEdit_auth_code.setObjectName(u"lineEdit_auth_code")

        self.verticalLayout_3.addWidget(self.lineEdit_auth_code)

        self.reg_frame = QFrame(self.auth_frame_main)
        self.reg_frame.setObjectName(u"reg_frame")
        self.reg_frame.setFrameShape(QFrame.StyledPanel)
        self.reg_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.reg_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_noacc = QLabel(self.reg_frame)
        self.label_noacc.setObjectName(u"label_noacc")

        self.horizontalLayout_7.addWidget(self.label_noacc)

        self.label_noacc_reg = QPushButton(self.reg_frame)
        self.label_noacc_reg.setObjectName(u"label_noacc_reg")
        self.label_noacc_reg.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	color:blue;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-decoration: underline;\n"
"	color:blue;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_noacc_reg)


        self.verticalLayout_3.addWidget(self.reg_frame, 0, Qt.AlignHCenter)

        self.pushButton_auth = QPushButton(self.auth_frame_main)
        self.pushButton_auth.setObjectName(u"pushButton_auth")
        self.pushButton_auth.setStyleSheet(u"QWidget{\n"
"background-color: #18181B;\n"
"color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_auth)


        self.gridLayout_2.addWidget(self.auth_frame_main, 2, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(150, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 1, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 1, 1, 2)

        self.frame_noacc_reg_up = QFrame(self.frame_auth_grid)
        self.frame_noacc_reg_up.setObjectName(u"frame_noacc_reg_up")
        font6 = QFont()
        font6.setPointSize(11)
        self.frame_noacc_reg_up.setFont(font6)
        self.frame_noacc_reg_up.setFrameShape(QFrame.StyledPanel)
        self.frame_noacc_reg_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_noacc_reg_up)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_noacc_reg_up = QPushButton(self.frame_noacc_reg_up)
        self.pushButton_noacc_reg_up.setObjectName(u"pushButton_noacc_reg_up")
        self.pushButton_noacc_reg_up.setFont(font5)
        self.pushButton_noacc_reg_up.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	color:black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-decoration: underline;\n"
"	color:black;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_noacc_reg_up)


        self.gridLayout_2.addWidget(self.frame_noacc_reg_up, 0, 0, 1, 4, Qt.AlignRight)


        self.horizontalLayout_8.addWidget(self.frame_auth_grid)

        self.stackedWidget.addWidget(self.authorization_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Authorization)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Authorization)
    # setupUi

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(QCoreApplication.translate("Authorization", u"Dialog", None))
        self.label_app_img.setText("")
        self.label_app_name.setText(QCoreApplication.translate("Authorization", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.label_app_quote.setText(QCoreApplication.translate("Authorization", u"\"\u041f\u043b\u0430\u043d - \u044d\u0442\u043e \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0443\u0441\u043f\u0435\u0445\u0430\".", None))
        self.label_app_author_quote.setText(QCoreApplication.translate("Authorization", u"\u0414\u0436\u043e\u0440\u0434\u0436 \u041a\u043b\u044e\u043a\u0430\u043d\u043e\u0432 \u044d\u043b\u044c \u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d", None))
        self.label_reg_main.setText(QCoreApplication.translate("Authorization", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.label_reg_email.setText(QCoreApplication.translate("Authorization", u"Email", None))
        self.lineEdit_reg_email.setPlaceholderText(QCoreApplication.translate("Authorization", u"addres@example.com", None))
        self.label_reg_f.setText(QCoreApplication.translate("Authorization", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_reg_f.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0416\u043c\u044b\u0448\u0435\u043d\u043a\u043e", None))
        self.label_reg_n.setText(QCoreApplication.translate("Authorization", u"\u0418\u043c\u044f", None))
        self.lineEdit_reg_n.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0412\u0430\u043b\u0435\u0440\u0438\u0439", None))
        self.label_reg_m.setText(QCoreApplication.translate("Authorization", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_reg_m.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0410\u043b\u044c\u0431\u0435\u0440\u0442\u043e\u0432\u0438\u0447", None))
        self.label_reg_url.setText(QCoreApplication.translate("Authorization", u"\u0410\u0434\u0440\u0435\u0441 \u0441\u0435\u0440\u0432\u0435\u0440 Nextcloud", None))
        self.lineEdit_reg_url_nc.setPlaceholderText(QCoreApplication.translate("Authorization", u"url", None))
        self.label_reg_calendar_name.setText(QCoreApplication.translate("Authorization", u"\u0418\u043c\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f", None))
        self.lineEdit_reg_calendar_name.setPlaceholderText(QCoreApplication.translate("Authorization", u"ExampleCalendar", None))
        self.label_reg_password1.setText(QCoreApplication.translate("Authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_reg_password2.setText(QCoreApplication.translate("Authorization", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_haveacc.setText(QCoreApplication.translate("Authorization", u"\u0415\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442?", None))
        self.pushButton_haveacc_auth.setText(QCoreApplication.translate("Authorization", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButton_reg.setText(QCoreApplication.translate("Authorization", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_haveacc_auth_up.setText(QCoreApplication.translate("Authorization", u"\u0412\u0445\u043e\u0434", None))
        self.label_auth_login.setText(QCoreApplication.translate("Authorization", u"\u0412\u0445\u043e\u0434 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label_auth_f.setText(QCoreApplication.translate("Authorization", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_auth_f.setText("")
        self.lineEdit_auth_f.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0416\u043c\u044b\u0448\u0435\u043d\u043a\u043e", None))
        self.label_auth_n.setText(QCoreApplication.translate("Authorization", u"\u0418\u043c\u044f", None))
        self.lineEdit_auth_n.setText("")
        self.lineEdit_auth_n.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0412\u0430\u043b\u0435\u0440\u0438\u0439", None))
        self.label_auth_m.setText(QCoreApplication.translate("Authorization", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_auth_m.setText("")
        self.lineEdit_auth_m.setPlaceholderText(QCoreApplication.translate("Authorization", u"\u0410\u043b\u044c\u0431\u0435\u0440\u0442\u043e\u0432\u0438\u0447", None))
        self.label_auth_email.setText(QCoreApplication.translate("Authorization", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.lineEdit_auth_email.setPlaceholderText(QCoreApplication.translate("Authorization", u"address@example.com", None))
        self.label_auth_code.setText(QCoreApplication.translate("Authorization", u"\u0428\u0438\u0444\u0440 \u0432\u0445\u043e\u0434\u0430", None))
        self.label_noacc.setText(QCoreApplication.translate("Authorization", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430?", None))
        self.label_noacc_reg.setText(QCoreApplication.translate("Authorization", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_auth.setText(QCoreApplication.translate("Authorization", u"\u0412\u0445\u043e\u0434 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.pushButton_noacc_reg_up.setText(QCoreApplication.translate("Authorization", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

