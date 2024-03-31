# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QToolBox, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1442, 612)
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
        self.user_frame = QFrame(self.centralwidget)
        self.user_frame.setObjectName(u"user_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.user_frame.sizePolicy().hasHeightForWidth())
        self.user_frame.setSizePolicy(sizePolicy2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy3)
        self.info_frame.setMinimumSize(QSize(596, 0))
        self.info_frame.setStyleSheet(u" QFrame{\n"
"  background-color: #08080a;\n"
" 	border: 2px solid rgb(85, 255, 0) ;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.info_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.info_frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_10.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addWidget(self.info_frame, 0, 5, 1, 1)

        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy4)
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
        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.tags_frame = QFrame(self.menu_frame)
        self.tags_frame.setObjectName(u"tags_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tags_frame.sizePolicy().hasHeightForWidth())
        self.tags_frame.setSizePolicy(sizePolicy5)
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


        self.gridLayout_3.addWidget(self.tags_frame, 5, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.menu_frame)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.treeWidget.setMinimumSize(QSize(0, 100))
        self.treeWidget.setStyleSheet(u"QWidget{\n"
"	width: 5px;\n"
"}\n"
"")
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)

        self.gridLayout_3.addWidget(self.treeWidget, 7, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.lists_frame = QFrame(self.menu_frame)
        self.lists_frame.setObjectName(u"lists_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lists_frame.sizePolicy().hasHeightForWidth())
        self.lists_frame.setSizePolicy(sizePolicy6)
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

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.buttons_frame = QFrame(self.menu_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        sizePolicy5.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy5)
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


        self.gridLayout_2.addWidget(self.menu_frame, 0, 1, 1, 1, Qt.AlignHCenter)

        self.tasks_frame = QFrame(self.centralwidget)
        self.tasks_frame.setObjectName(u"tasks_frame")
        sizePolicy3.setHeightForWidth(self.tasks_frame.sizePolicy().hasHeightForWidth())
        self.tasks_frame.setSizePolicy(sizePolicy3)
        self.tasks_frame.setMinimumSize(QSize(596, 0))
        self.tasks_frame.setStyleSheet(u" QFrame{\n"
"  background-color: #08080a;\n"
" 	border: 2px solid rgb(255, 170, 0);\n"
"}")
        self.tasks_frame.setFrameShape(QFrame.StyledPanel)
        self.tasks_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.tasks_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.verticalSpacer_2 = QSpacerItem(20, 700, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 7, 0, 1, 2)

        self.frame_3 = QFrame(self.tasks_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy7)
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy8)
        self.pushButton_4.setMinimumSize(QSize(29, 30))
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_3)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy9)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy10)
        self.comboBox.setMaximumSize(QSize(30, 30))
        self.comboBox.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")
        self.comboBox.setFrame(True)

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.horizontalLayout.addWidget(self.frame_2)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.tasks_frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 400))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolBox = QToolBox(self.frame_6)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy7.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy7)
        self.toolBox.setMinimumSize(QSize(0, 200))
        self.toolBox.setMaximumSize(QSize(16777215, 300))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 544, 192))
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_3 = QTreeWidget(self.page)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget_3)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.treeWidget_3.setObjectName(u"treeWidget_3")
        self.treeWidget_3.setHeaderHidden(True)
        self.treeWidget_3.header().setDefaultSectionSize(200)

        self.verticalLayout_8.addWidget(self.treeWidget_3)

        self.toolBox.addItem(self.page, u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e, <X>")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 544, 192))
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_2 = QTreeWidget(self.page_2)
        __qtreewidgetitem5 = QTreeWidgetItem(self.treeWidget_2)
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget_2)
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setHeaderHidden(True)
        self.treeWidget_2.header().setDefaultSectionSize(200)

        self.verticalLayout_4.addWidget(self.treeWidget_2)

        self.toolBox.addItem(self.page_2, u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435, <X>")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 544, 192))
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_4 = QTreeWidget(self.page_3)
        __qtreewidgetitem10 = QTreeWidgetItem(self.treeWidget_4)
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem11)
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13 = QTreeWidgetItem(self.treeWidget_4)
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem13)
        QTreeWidgetItem(__qtreewidgetitem14)
        self.treeWidget_4.setObjectName(u"treeWidget_4")
        self.treeWidget_4.setHeaderHidden(True)
        self.treeWidget_4.header().setDefaultSectionSize(200)

        self.verticalLayout_9.addWidget(self.treeWidget_4)

        self.toolBox.addItem(self.page_3, u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e, <X>")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)


        self.gridLayout_4.addWidget(self.frame_6, 5, 0, 2, 2, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.frame = QFrame(self.tasks_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(100)
        sizePolicy11.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy11)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setStyleSheet(u"QFrame{\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QWidget::hover{\n"
"border:1px solid white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(50, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"border: 0px solid gray;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color:transparent; \n"
"border: 0px transparent;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy7.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy7)
        self.pushButton_7.setMinimumSize(QSize(30, 16))
        self.pushButton_7.setMaximumSize(QSize(20, 16777215))
        self.pushButton_7.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy7.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy7)
        self.pushButton_8.setMinimumSize(QSize(30, 16))
        self.pushButton_8.setMaximumSize(QSize(20, 16777215))
        self.pushButton_8.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy7.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy7)
        self.pushButton_6.setMinimumSize(QSize(30, 16))
        self.pushButton_6.setMaximumSize(QSize(20, 16777215))
        self.pushButton_6.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy7.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy7)
        self.pushButton_5.setMinimumSize(QSize(50, 16))
        self.pushButton_5.setMaximumSize(QSize(20, 16777215))
        self.pushButton_5.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 3, 0, 1, 2)


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

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.account_button.setText(QCoreApplication.translate("MainWindow", u"avatar", None))
        self.calendar_button.setText(QCoreApplication.translate("MainWindow", u"calendar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0443, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0435\u0451...", None))
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

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u04401", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u04402", None))

        ___qtreewidgetitem7 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled1 = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        ___qtreewidgetitem8 = self.treeWidget_3.topLevelItem(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, 3 \u0434\u043d\u044f \u043d\u0430\u0437\u0430\u0434", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        self.treeWidget_3.setSortingEnabled(__sortingEnabled1)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e, <X>", None))
        ___qtreewidgetitem11 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem11.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled2 = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem12 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem13.child(1)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 1", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem12.child(1)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem16.child(1)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 2", None));
        ___qtreewidgetitem19 = self.treeWidget_2.topLevelItem(1)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, \u0437\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem20.child(0)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem20.child(1)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 3", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled2)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435, <X>", None))
        ___qtreewidgetitem23 = self.treeWidget_4.headerItem()
        ___qtreewidgetitem23.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled3 = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        ___qtreewidgetitem24 = self.treeWidget_4.topLevelItem(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem24.child(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem24.child(1)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem27.child(0)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem29 = self.treeWidget_4.topLevelItem(1)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, \u0437\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem29.child(0)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem30.child(0)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        self.treeWidget_4.setSortingEnabled(__sortingEnabled3)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e, <X>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433\u0438", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u0430\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0442\u043e", None))
    # retranslateUi

