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
        MainWindow.resize(1495, 584)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
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


        self.gridLayout_3.addWidget(self.tags_frame, 4, 0, 1, 1)

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


        self.gridLayout_3.addWidget(self.lists_frame, 1, 0, 1, 1)

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

        self.gridLayout_3.addWidget(self.treeWidget, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 8, 0, 1, 1)


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
        self.frame_info = QFrame(self.tasks_frame)
        self.frame_info.setObjectName(u"frame_info")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_info.sizePolicy().hasHeightForWidth())
        self.frame_info.setSizePolicy(sizePolicy7)
        self.frame_info.setMinimumSize(QSize(40, 0))
        self.frame_info.setMaximumSize(QSize(16777215, 50))
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_info)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_panel_close = QPushButton(self.frame_info)
        self.pushButton_panel_close.setObjectName(u"pushButton_panel_close")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_panel_close.sizePolicy().hasHeightForWidth())
        self.pushButton_panel_close.setSizePolicy(sizePolicy8)
        self.pushButton_panel_close.setMinimumSize(QSize(29, 30))
        self.pushButton_panel_close.setMaximumSize(QSize(30, 30))
        self.pushButton_panel_close.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_panel_close)

        self.label_info_week = QLabel(self.frame_info)
        self.label_info_week.setObjectName(u"label_info_week")
        sizePolicy1.setHeightForWidth(self.label_info_week.sizePolicy().hasHeightForWidth())
        self.label_info_week.setSizePolicy(sizePolicy1)
        self.label_info_week.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.label_info_week)

        self.comboBox_tasks_filters = QComboBox(self.frame_info)
        self.comboBox_tasks_filters.addItem("")
        self.comboBox_tasks_filters.addItem("")
        self.comboBox_tasks_filters.addItem("")
        self.comboBox_tasks_filters.setObjectName(u"comboBox_tasks_filters")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.comboBox_tasks_filters.sizePolicy().hasHeightForWidth())
        self.comboBox_tasks_filters.setSizePolicy(sizePolicy9)
        self.comboBox_tasks_filters.setMaximumSize(QSize(30, 30))
        self.comboBox_tasks_filters.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")
        self.comboBox_tasks_filters.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_tasks_filters)


        self.gridLayout_4.addWidget(self.frame_info, 0, 0, 1, 1)

        self.frame_adding_grid = QFrame(self.tasks_frame)
        self.frame_adding_grid.setObjectName(u"frame_adding_grid")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(100)
        sizePolicy10.setHeightForWidth(self.frame_adding_grid.sizePolicy().hasHeightForWidth())
        self.frame_adding_grid.setSizePolicy(sizePolicy10)
        self.frame_adding_grid.setMinimumSize(QSize(0, 0))
        self.frame_adding_grid.setFrameShape(QFrame.StyledPanel)
        self.frame_adding_grid.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_adding_grid)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.frame_adding_border = QFrame(self.frame_adding_grid)
        self.frame_adding_border.setObjectName(u"frame_adding_border")
        sizePolicy6.setHeightForWidth(self.frame_adding_border.sizePolicy().hasHeightForWidth())
        self.frame_adding_border.setSizePolicy(sizePolicy6)
        self.frame_adding_border.setStyleSheet(u"QFrame{\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QWidget::hover{\n"
"border:1px solid white;\n"
"}")
        self.frame_adding_border.setFrameShape(QFrame.StyledPanel)
        self.frame_adding_border.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_adding_border)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_add_task = QLineEdit(self.frame_adding_border)
        self.lineEdit_add_task.setObjectName(u"lineEdit_add_task")
        sizePolicy1.setHeightForWidth(self.lineEdit_add_task.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_task.setSizePolicy(sizePolicy1)
        self.lineEdit_add_task.setMinimumSize(QSize(50, 40))
        self.lineEdit_add_task.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_add_task.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"border: 0px solid gray;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.lineEdit_add_task)

        self.frame__adding_buttons = QFrame(self.frame_adding_border)
        self.frame__adding_buttons.setObjectName(u"frame__adding_buttons")
        self.frame__adding_buttons.setStyleSheet(u"QFrame{\n"
"background-color:transparent; \n"
"border: 0px transparent;\n"
"}")
        self.frame__adding_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame__adding_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame__adding_buttons)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.pushButton_tags = QPushButton(self.frame__adding_buttons)
        self.pushButton_tags.setObjectName(u"pushButton_tags")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.pushButton_tags.sizePolicy().hasHeightForWidth())
        self.pushButton_tags.setSizePolicy(sizePolicy11)
        self.pushButton_tags.setMinimumSize(QSize(30, 16))
        self.pushButton_tags.setMaximumSize(QSize(20, 16777215))
        self.pushButton_tags.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_tags)

        self.pushButton_assign = QPushButton(self.frame__adding_buttons)
        self.pushButton_assign.setObjectName(u"pushButton_assign")
        sizePolicy11.setHeightForWidth(self.pushButton_assign.sizePolicy().hasHeightForWidth())
        self.pushButton_assign.setSizePolicy(sizePolicy11)
        self.pushButton_assign.setMinimumSize(QSize(30, 16))
        self.pushButton_assign.setMaximumSize(QSize(20, 16777215))
        self.pushButton_assign.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_assign)

        self.pushButton_data = QPushButton(self.frame__adding_buttons)
        self.pushButton_data.setObjectName(u"pushButton_data")
        sizePolicy11.setHeightForWidth(self.pushButton_data.sizePolicy().hasHeightForWidth())
        self.pushButton_data.setSizePolicy(sizePolicy11)
        self.pushButton_data.setMinimumSize(QSize(30, 16))
        self.pushButton_data.setMaximumSize(QSize(20, 16777215))
        self.pushButton_data.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_data)

        self.pushButton_create = QPushButton(self.frame__adding_buttons)
        self.pushButton_create.setObjectName(u"pushButton_create")
        sizePolicy11.setHeightForWidth(self.pushButton_create.sizePolicy().hasHeightForWidth())
        self.pushButton_create.setSizePolicy(sizePolicy11)
        self.pushButton_create.setMinimumSize(QSize(50, 16))
        self.pushButton_create.setMaximumSize(QSize(20, 16777215))
        self.pushButton_create.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_create)


        self.horizontalLayout_4.addWidget(self.frame__adding_buttons)


        self.gridLayout_5.addWidget(self.frame_adding_border, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_adding_grid, 1, 0, 1, 1)

        self.toolBox = QToolBox(self.tasks_frame)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy11.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy11)
        self.toolBox.setMinimumSize(QSize(0, 200))
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.page_overdue = QWidget()
        self.page_overdue.setObjectName(u"page_overdue")
        self.page_overdue.setGeometry(QRect(0, 0, 593, 245))
        self.verticalLayout_8 = QVBoxLayout(self.page_overdue)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_overdue = QTreeWidget(self.page_overdue)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget_overdue)
        __qtreewidgetitem3.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.treeWidget_overdue.setObjectName(u"treeWidget_overdue")
        self.treeWidget_overdue.setAnimated(True)
        self.treeWidget_overdue.setHeaderHidden(True)
        self.treeWidget_overdue.header().setDefaultSectionSize(200)

        self.verticalLayout_8.addWidget(self.treeWidget_overdue)

        self.toolBox.addItem(self.page_overdue, u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e, <X>")
        self.page_current = QWidget()
        self.page_current.setObjectName(u"page_current")
        self.page_current.setGeometry(QRect(0, 0, 593, 245))
        self.verticalLayout_4 = QVBoxLayout(self.page_current)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_current = QTreeWidget(self.page_current)
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget_current)
        __qtreewidgetitem6.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem9.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem11 = QTreeWidgetItem(self.treeWidget_current)
        __qtreewidgetitem11.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem11)
        __qtreewidgetitem12.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.treeWidget_current.setObjectName(u"treeWidget_current")
        self.treeWidget_current.setAutoFillBackground(False)
        self.treeWidget_current.setStyleSheet(u"")
        self.treeWidget_current.setAnimated(True)
        self.treeWidget_current.setAllColumnsShowFocus(False)
        self.treeWidget_current.setHeaderHidden(True)
        self.treeWidget_current.header().setCascadingSectionResizes(True)
        self.treeWidget_current.header().setDefaultSectionSize(417)
        self.treeWidget_current.header().setProperty("showSortIndicator", False)

        self.verticalLayout_4.addWidget(self.treeWidget_current)

        self.toolBox.addItem(self.page_current, u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435, <X>")
        self.page_completed = QWidget()
        self.page_completed.setObjectName(u"page_completed")
        self.page_completed.setGeometry(QRect(0, 0, 593, 245))
        self.verticalLayout_9 = QVBoxLayout(self.page_completed)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_completed = QTreeWidget(self.page_completed)
        __qtreewidgetitem14 = QTreeWidgetItem(self.treeWidget_completed)
        __qtreewidgetitem14.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem15 = QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem15)
        __qtreewidgetitem16 = QTreeWidgetItem(__qtreewidgetitem15)
        __qtreewidgetitem16.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem17 = QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem17)
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem17)
        __qtreewidgetitem18.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem19 = QTreeWidgetItem(self.treeWidget_completed)
        __qtreewidgetitem19.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem20 = QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem20)
        __qtreewidgetitem21 = QTreeWidgetItem(__qtreewidgetitem20)
        __qtreewidgetitem21.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.treeWidget_completed.setObjectName(u"treeWidget_completed")
        self.treeWidget_completed.setAnimated(True)
        self.treeWidget_completed.setHeaderHidden(True)
        self.treeWidget_completed.header().setDefaultSectionSize(200)

        self.verticalLayout_9.addWidget(self.treeWidget_completed)

        self.toolBox.addItem(self.page_completed, u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e, <X>")

        self.gridLayout_4.addWidget(self.toolBox, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.tasks_frame, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 1495, 21))
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

        self.toolBox.setCurrentIndex(2)
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
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438", None))
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

        self.pushButton_panel_close.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.label_info_week.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))
        self.comboBox_tasks_filters.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.comboBox_tasks_filters.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u04401", None))
        self.comboBox_tasks_filters.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u04402", None))

        self.lineEdit_add_task.setText("")
        self.lineEdit_add_task.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pushButton_tags.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433\u0438", None))
        self.pushButton_assign.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u0430\u0442\u044c", None))
        self.pushButton_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.pushButton_create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        ___qtreewidgetitem7 = self.treeWidget_overdue.headerItem()
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled1 = self.treeWidget_overdue.isSortingEnabled()
        self.treeWidget_overdue.setSortingEnabled(False)
        ___qtreewidgetitem8 = self.treeWidget_overdue.topLevelItem(0)
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, 3 \u0434\u043d\u044f \u043d\u0430\u0437\u0430\u0434", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem9.child(1)
        ___qtreewidgetitem11.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04331", None));
        self.treeWidget_overdue.setSortingEnabled(__sortingEnabled1)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_overdue), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e, <X>", None))
        ___qtreewidgetitem12 = self.treeWidget_current.headerItem()
        ___qtreewidgetitem12.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled2 = self.treeWidget_current.isSortingEnabled()
        self.treeWidget_current.setSortingEnabled(False)
        ___qtreewidgetitem13 = self.treeWidget_current.topLevelItem(0)
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem14.child(0)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem14.child(1)
        ___qtreewidgetitem16.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 1", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem13.child(1)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem17.child(1)
        ___qtreewidgetitem19.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 2", None));
        ___qtreewidgetitem20 = self.treeWidget_current.topLevelItem(1)
        ___qtreewidgetitem20.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, \u0437\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem20.child(0)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem21.child(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem21.child(1)
        ___qtreewidgetitem23.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 3", None));
        self.treeWidget_current.setSortingEnabled(__sortingEnabled2)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_current), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435, <X>", None))
        ___qtreewidgetitem24 = self.treeWidget_completed.headerItem()
        ___qtreewidgetitem24.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled3 = self.treeWidget_completed.isSortingEnabled()
        self.treeWidget_completed.setSortingEnabled(False)
        ___qtreewidgetitem25 = self.treeWidget_completed.topLevelItem(0)
        ___qtreewidgetitem25.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem26.child(0)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem26.child(1)
        ___qtreewidgetitem28.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04331", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem25.child(1)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem29.child(0)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem29.child(1)
        ___qtreewidgetitem31.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04332", None));
        ___qtreewidgetitem32 = self.treeWidget_completed.topLevelItem(1)
        ___qtreewidgetitem32.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, \u0437\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem32.child(0)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem33.child(0)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem33.child(1)
        ___qtreewidgetitem35.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.treeWidget_completed.setSortingEnabled(__sortingEnabled3)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_completed), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e, <X>", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0442\u043e", None))
    # retranslateUi

