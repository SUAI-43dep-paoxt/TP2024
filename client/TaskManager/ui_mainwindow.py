# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1442, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QWidget{\n"
" color: white;\n"
"}\n"
"")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setStyleSheet(u" QFrame{\n"
"  background-color: #08080a;\n"
" 	border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.menu_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.lists_frame = QFrame(self.menu_frame)
        self.lists_frame.setObjectName(u"lists_frame")
        sizePolicy1.setHeightForWidth(self.lists_frame.sizePolicy().hasHeightForWidth())
        self.lists_frame.setSizePolicy(sizePolicy1)
        self.lists_frame.setMinimumSize(QSize(0, 40))
        self.lists_frame.setFrameShape(QFrame.StyledPanel)
        self.lists_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.lists_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.lists_frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"QLabel{\n"
"border: 0px;\n"
"}")

        self.verticalLayout_5.addWidget(self.label)


        self.gridLayout_3.addWidget(self.lists_frame, 2, 0, 1, 1)

        self.buttons_frame = QFrame(self.menu_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        sizePolicy1.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy1)
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_3 = QPushButton(self.buttons_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.buttons_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.buttons_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.gridLayout_3.addWidget(self.buttons_frame, 0, 0, 1, 1)

        self.tags_frame = QFrame(self.menu_frame)
        self.tags_frame.setObjectName(u"tags_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tags_frame.sizePolicy().hasHeightForWidth())
        self.tags_frame.setSizePolicy(sizePolicy2)
        self.tags_frame.setStyleSheet(u"")
        self.tags_frame.setFrameShape(QFrame.StyledPanel)
        self.tags_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.tags_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.tags_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"border: 0px;\n"
"}")

        self.verticalLayout.addWidget(self.label_2)

        self.treeWidget = QTreeWidget(self.tags_frame)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.treeWidget.setStyleSheet(u"QWidget{\n"
"	color:red;\n"
"	width: 5px;\n"
"}\n"
"")
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)

        self.verticalLayout.addWidget(self.treeWidget)


        self.gridLayout_3.addWidget(self.tags_frame, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 500, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.menu_frame, 0, 1, 1, 1, Qt.AlignHCenter)

        self.user_frame = QFrame(self.centralwidget)
        self.user_frame.setObjectName(u"user_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.user_frame.sizePolicy().hasHeightForWidth())
        self.user_frame.setSizePolicy(sizePolicy3)
        self.user_frame.setMinimumSize(QSize(48, 0))
        self.user_frame.setMaximumSize(QSize(16777215, 16777215))
        self.user_frame.setStyleSheet(u" QFrame{\n"
"  background-color: #08080a;\n"
" 	border: 2px solid rgb(255, 0, 0) ;\n"
"}")
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.user_frame)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.user_items_frame = QFrame(self.user_frame)
        self.user_items_frame.setObjectName(u"user_items_frame")
        sizePolicy1.setHeightForWidth(self.user_items_frame.sizePolicy().hasHeightForWidth())
        self.user_items_frame.setSizePolicy(sizePolicy1)
        self.user_items_frame.setFrameShape(QFrame.StyledPanel)
        self.user_items_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.user_items_frame)
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.account_button = QPushButton(self.user_items_frame)
        self.account_button.setObjectName(u"account_button")

        self.verticalLayout_7.addWidget(self.account_button)

        self.calendar_button = QPushButton(self.user_items_frame)
        self.calendar_button.setObjectName(u"calendar_button")

        self.verticalLayout_7.addWidget(self.calendar_button)


        self.verticalLayout_6.addWidget(self.user_items_frame)

        self.verticalSpacer_4 = QSpacerItem(20, 800, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addWidget(self.user_frame, 0, 0, 1, 1)

        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(15)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy4)
        self.info_frame.setMinimumSize(QSize(596, 0))
        self.info_frame.setStyleSheet(u" QFrame{\n"
"  background-color: #08080a;\n"
" 	border: 2px solid rgb(85, 255, 0) ;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.info_frame, 0, 5, 1, 1)

        self.tasks_frame = QFrame(self.centralwidget)
        self.tasks_frame.setObjectName(u"tasks_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(15)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.tasks_frame.sizePolicy().hasHeightForWidth())
        self.tasks_frame.setSizePolicy(sizePolicy5)
        self.tasks_frame.setMinimumSize(QSize(596, 0))
        self.tasks_frame.setStyleSheet(u" QFrame{\n"
"  background-color: #08080a;\n"
" 	border: 2px solid rgb(255, 170, 0);\n"
"}")
        self.tasks_frame.setFrameShape(QFrame.StyledPanel)
        self.tasks_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.tasks_frame, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 1442, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        icon = QIcon(QIcon.fromTheme(u"accessories-character-map"))
        self.menu.setIcon(icon)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043a\u0438 / \u0422\u0435\u0433\u0438", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u0433\u0430", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0435\u0433", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"\u041a\u0440", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"\u0416\u0435\u043b", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0435\u0433", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 3", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0435\u0433", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.account_button.setText(QCoreApplication.translate("MainWindow", u"avatar", None))
        self.calendar_button.setText(QCoreApplication.translate("MainWindow", u"calendar", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0442\u043e", None))
    # retranslateUi

