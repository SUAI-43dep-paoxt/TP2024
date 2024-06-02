# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acceptionWin.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AcceptionWin(object):
    def setupUi(self, AcceptionWin):
        if not AcceptionWin.objectName():
            AcceptionWin.setObjectName(u"AcceptionWin")
        AcceptionWin.setWindowModality(Qt.ApplicationModal)
        AcceptionWin.resize(337, 178)
        AcceptionWin.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 37);\n"
"	color: white;\n"
"}\n"
"QPushButton{\n"
"	background-color: white;\n"
"	border:1px solid rgb(70,70,70);\n"
"    border-radius: 4px;\n"
"	color: black;\n"
"	padding: 110px;\n"
"	width:50px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	border:1px;\n"
"	background-color: rgb(180,180,180);\n"
"}\n"
"")
        AcceptionWin.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(AcceptionWin)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(AcceptionWin)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_info = QFrame(self.frame)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_warning = QLabel(self.frame_info)
        self.label_warning.setObjectName(u"label_warning")
        self.label_warning.setFont(font)
        self.label_warning.setStyleSheet(u"border:0px;")
        self.label_warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_warning)

        self.line = QFrame(self.frame_info)
        self.line.setObjectName(u"line")
        self.line.setFont(font)
        self.line.setStyleSheet(u"border:0px;\n"
"border-top: 1px solid white;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_4 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_description = QLabel(self.frame_info)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setFont(font)
        self.label_description.setStyleSheet(u"border:0px;")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_description)

        self.verticalSpacer_5 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.line_2 = QFrame(self.frame_info)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font)
        self.line_2.setStyleSheet(u"border:0px;\n"
"border-top: 1px solid white;")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_description.raise_()
        self.label_warning.raise_()
        self.line.raise_()
        self.line_2.raise_()

        self.verticalLayout_2.addWidget(self.frame_info)

        self.frame_buttons = QFrame(self.frame)
        self.frame_buttons.setObjectName(u"frame_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy)
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setMinimumSize(QSize(150, 25))
        self.buttonBox.setMaximumSize(QSize(70, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.buttonBox.setFont(font1)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.frame_buttons)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.retranslateUi(AcceptionWin)

        QMetaObject.connectSlotsByName(AcceptionWin)
    # setupUi

    def retranslateUi(self, AcceptionWin):
        AcceptionWin.setWindowTitle(QCoreApplication.translate("AcceptionWin", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.label_warning.setText(QCoreApplication.translate("AcceptionWin", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435", None))
        self.label_description.setText(QCoreApplication.translate("AcceptionWin", u"[\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f]", None))
    # retranslateUi

