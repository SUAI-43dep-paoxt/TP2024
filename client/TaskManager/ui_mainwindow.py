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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolBox, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1442, 651)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QFrame{\n"
"background-color: transparent;\n"
"border: 0px solid gray;\n"
"}\n"
"\n"
"QWidget{\n"
" color: white;\n"
"background-color: #09090B;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"border: 0px solid gray;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: transparent;\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border: 0px solid white;\n"
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
        self.centralwidget.setStyleSheet(u"")
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy2)
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setStyleSheet(u"#menu_frame {\n"
"    border-left: 1px solid grey;\n"
"}")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.menu_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.treeWidget = QTreeWidget(self.menu_frame)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
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

        self.gridLayout_3.addWidget(self.treeWidget, 4, 0, 1, 1)

        self.tags_frame = QFrame(self.menu_frame)
        self.tags_frame.setObjectName(u"tags_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tags_frame.sizePolicy().hasHeightForWidth())
        self.tags_frame.setSizePolicy(sizePolicy3)
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


        self.gridLayout_3.addWidget(self.tags_frame, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.buttons_frame = QFrame(self.menu_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        sizePolicy3.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy3)
        self.buttons_frame.setStyleSheet(u"#buttons_frame {\n"
"    border-bottom: 1px solid gray;\n"
"}")
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

        self.user_frame = QFrame(self.centralwidget)
        self.user_frame.setObjectName(u"user_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.user_frame.sizePolicy().hasHeightForWidth())
        self.user_frame.setSizePolicy(sizePolicy4)
        self.user_frame.setMinimumSize(QSize(48, 0))
        self.user_frame.setMaximumSize(QSize(16777215, 16777215))
        self.user_frame.setStyleSheet(u"")
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.user_frame)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.user_items_frame = QFrame(self.user_frame)
        self.user_items_frame.setObjectName(u"user_items_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.user_items_frame.sizePolicy().hasHeightForWidth())
        self.user_items_frame.setSizePolicy(sizePolicy5)
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

        self.invite_button = QPushButton(self.user_items_frame)
        self.invite_button.setObjectName(u"invite_button")

        self.verticalLayout_7.addWidget(self.invite_button)


        self.verticalLayout_6.addWidget(self.user_items_frame)

        self.verticalSpacer_4 = QSpacerItem(20, 800, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addWidget(self.user_frame, 0, 0, 1, 1)

        self.tasks_frame = QFrame(self.centralwidget)
        self.tasks_frame.setObjectName(u"tasks_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(15)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.tasks_frame.sizePolicy().hasHeightForWidth())
        self.tasks_frame.setSizePolicy(sizePolicy6)
        self.tasks_frame.setMinimumSize(QSize(596, 0))
        self.tasks_frame.setStyleSheet(u"#tasks_frame {\n"
"    border-left: 1px solid grey;\n"
"}")
        self.tasks_frame.setFrameShape(QFrame.StyledPanel)
        self.tasks_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.tasks_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_adding_grid = QFrame(self.tasks_frame)
        self.frame_adding_grid.setObjectName(u"frame_adding_grid")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(100)
        sizePolicy7.setHeightForWidth(self.frame_adding_grid.sizePolicy().hasHeightForWidth())
        self.frame_adding_grid.setSizePolicy(sizePolicy7)
        self.frame_adding_grid.setMinimumSize(QSize(0, 0))
        self.frame_adding_grid.setFrameShape(QFrame.StyledPanel)
        self.frame_adding_grid.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_adding_grid)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.frame_adding_border = QFrame(self.frame_adding_grid)
        self.frame_adding_border.setObjectName(u"frame_adding_border")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_adding_border.sizePolicy().hasHeightForWidth())
        self.frame_adding_border.setSizePolicy(sizePolicy8)
        self.frame_adding_border.setStyleSheet(u"#frame_adding_border{\n"
"    border: 1px solid grey;\n"
"	border-radius: 10px;\n"
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
        self.lineEdit_add_task.setStyleSheet(u"QLineEdit:hover{\n"
"border:0px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEdit_add_task)

        self.frame__adding_buttons = QFrame(self.frame_adding_border)
        self.frame__adding_buttons.setObjectName(u"frame__adding_buttons")
        self.frame__adding_buttons.setStyleSheet(u"")
        self.frame__adding_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame__adding_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame__adding_buttons)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.pushButton_tags = QPushButton(self.frame__adding_buttons)
        self.pushButton_tags.setObjectName(u"pushButton_tags")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_tags.sizePolicy().hasHeightForWidth())
        self.pushButton_tags.setSizePolicy(sizePolicy9)
        self.pushButton_tags.setMinimumSize(QSize(30, 16))
        self.pushButton_tags.setMaximumSize(QSize(20, 16777215))
        self.pushButton_tags.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_tags)

        self.pushButton_assign = QPushButton(self.frame__adding_buttons)
        self.pushButton_assign.setObjectName(u"pushButton_assign")
        sizePolicy9.setHeightForWidth(self.pushButton_assign.sizePolicy().hasHeightForWidth())
        self.pushButton_assign.setSizePolicy(sizePolicy9)
        self.pushButton_assign.setMinimumSize(QSize(30, 16))
        self.pushButton_assign.setMaximumSize(QSize(20, 16777215))
        self.pushButton_assign.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_assign)

        self.pushButton_data = QPushButton(self.frame__adding_buttons)
        self.pushButton_data.setObjectName(u"pushButton_data")
        sizePolicy9.setHeightForWidth(self.pushButton_data.sizePolicy().hasHeightForWidth())
        self.pushButton_data.setSizePolicy(sizePolicy9)
        self.pushButton_data.setMinimumSize(QSize(30, 16))
        self.pushButton_data.setMaximumSize(QSize(20, 16777215))
        self.pushButton_data.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_data)

        self.pushButton_create = QPushButton(self.frame__adding_buttons)
        self.pushButton_create.setObjectName(u"pushButton_create")
        sizePolicy9.setHeightForWidth(self.pushButton_create.sizePolicy().hasHeightForWidth())
        self.pushButton_create.setSizePolicy(sizePolicy9)
        self.pushButton_create.setMinimumSize(QSize(50, 16))
        self.pushButton_create.setMaximumSize(QSize(20, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.pushButton_create.setFont(font)
        self.pushButton_create.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_create)


        self.horizontalLayout_4.addWidget(self.frame__adding_buttons)


        self.gridLayout_5.addWidget(self.frame_adding_border, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_adding_grid, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.frame_info = QFrame(self.tasks_frame)
        self.frame_info.setObjectName(u"frame_info")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_info.sizePolicy().hasHeightForWidth())
        self.frame_info.setSizePolicy(sizePolicy10)
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
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.pushButton_panel_close.sizePolicy().hasHeightForWidth())
        self.pushButton_panel_close.setSizePolicy(sizePolicy11)
        self.pushButton_panel_close.setMinimumSize(QSize(29, 30))
        self.pushButton_panel_close.setMaximumSize(QSize(30, 30))
        self.pushButton_panel_close.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_panel_close)

        self.label_info_week = QLabel(self.frame_info)
        self.label_info_week.setObjectName(u"label_info_week")
        sizePolicy10.setHeightForWidth(self.label_info_week.sizePolicy().hasHeightForWidth())
        self.label_info_week.setSizePolicy(sizePolicy10)
        self.label_info_week.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.label_info_week)

        self.comboBox_tasks_filters = QComboBox(self.frame_info)
        self.comboBox_tasks_filters.addItem("")
        self.comboBox_tasks_filters.addItem("")
        self.comboBox_tasks_filters.addItem("")
        self.comboBox_tasks_filters.setObjectName(u"comboBox_tasks_filters")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.comboBox_tasks_filters.sizePolicy().hasHeightForWidth())
        self.comboBox_tasks_filters.setSizePolicy(sizePolicy12)
        self.comboBox_tasks_filters.setMaximumSize(QSize(30, 30))
        self.comboBox_tasks_filters.setStyleSheet(u"QWidget{\n"
"background-color: transparent;\n"
"border: none;\n"
"}")
        self.comboBox_tasks_filters.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox_tasks_filters)


        self.gridLayout_4.addWidget(self.frame_info, 0, 0, 1, 1)

        self.toolBox = QToolBox(self.tasks_frame)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy9.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy9)
        self.toolBox.setMinimumSize(QSize(0, 200))
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.page_overdue = QWidget()
        self.page_overdue.setObjectName(u"page_overdue")
        self.page_overdue.setGeometry(QRect(0, 0, 577, 338))
        self.verticalLayout_8 = QVBoxLayout(self.page_overdue)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_overdue = QTreeWidget(self.page_overdue)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_overdue)
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.treeWidget_overdue.setObjectName(u"treeWidget_overdue")
        self.treeWidget_overdue.setStyleSheet(u"QTreeView::branch {\n"
"        background: palette(base);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"        background: cyan;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"        background: red;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"        background: blue;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        background: pink;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"        background: gray;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"        background: magenta;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"        background: green;\n"
"}")
        self.treeWidget_overdue.setAnimated(True)
        self.treeWidget_overdue.setHeaderHidden(True)
        self.treeWidget_overdue.header().setDefaultSectionSize(200)

        self.verticalLayout_8.addWidget(self.treeWidget_overdue)

        self.toolBox.addItem(self.page_overdue, u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e, <X>")
        self.page_current = QWidget()
        self.page_current.setObjectName(u"page_current")
        self.page_current.setGeometry(QRect(0, 0, 577, 338))
        self.verticalLayout_4 = QVBoxLayout(self.page_current)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_current = QTreeWidget(self.page_current)
        brush = QBrush(QColor(255, 0, 4, 255))
        brush.setStyle(Qt.SolidPattern)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget_current)
        __qtreewidgetitem3.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        __qtreewidgetitem4.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem4.setCheckState(0, Qt.Checked);
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem5.setForeground(1, brush1);
        __qtreewidgetitem5.setBackground(0, brush);
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem6.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget_current)
        __qtreewidgetitem8.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem9.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.treeWidget_current.setObjectName(u"treeWidget_current")
        self.treeWidget_current.setAutoFillBackground(False)
        self.treeWidget_current.setStyleSheet(u"")
        self.treeWidget_current.setUniformRowHeights(False)
        self.treeWidget_current.setAnimated(True)
        self.treeWidget_current.setAllColumnsShowFocus(False)
        self.treeWidget_current.setWordWrap(False)
        self.treeWidget_current.setHeaderHidden(True)
        self.treeWidget_current.header().setVisible(False)
        self.treeWidget_current.header().setCascadingSectionResizes(True)
        self.treeWidget_current.header().setDefaultSectionSize(417)
        self.treeWidget_current.header().setProperty("showSortIndicator", False)

        self.verticalLayout_4.addWidget(self.treeWidget_current)

        self.toolBox.addItem(self.page_current, u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435, <X>")
        self.page_completed = QWidget()
        self.page_completed.setObjectName(u"page_completed")
        self.page_completed.setGeometry(QRect(0, 0, 577, 338))
        self.verticalLayout_9 = QVBoxLayout(self.page_completed)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_completed = QTreeWidget(self.page_completed)
        __qtreewidgetitem11 = QTreeWidgetItem(self.treeWidget_completed)
        __qtreewidgetitem11.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem14)
        __qtreewidgetitem15 = QTreeWidgetItem(__qtreewidgetitem14)
        __qtreewidgetitem15.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem16 = QTreeWidgetItem(self.treeWidget_completed)
        __qtreewidgetitem16.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem17 = QTreeWidgetItem(__qtreewidgetitem16)
        QTreeWidgetItem(__qtreewidgetitem17)
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem17)
        __qtreewidgetitem18.setTextAlignment(1, Qt.AlignTrailing|Qt.AlignVCenter);
        self.treeWidget_completed.setObjectName(u"treeWidget_completed")
        self.treeWidget_completed.setAnimated(True)
        self.treeWidget_completed.setHeaderHidden(True)
        self.treeWidget_completed.header().setDefaultSectionSize(200)

        self.verticalLayout_9.addWidget(self.treeWidget_completed)

        self.toolBox.addItem(self.page_completed, u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e, <X>")

        self.gridLayout_4.addWidget(self.toolBox, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.tasks_frame, 0, 4, 1, 1)

        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        sizePolicy6.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy6)
        self.info_frame.setMinimumSize(QSize(596, 0))
        self.info_frame.setStyleSheet(u"#info_frame {\n"
"    border-left: 1px solid grey;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.info_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.info_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_empty = QWidget()
        self.page_empty.setObjectName(u"page_empty")
        self.verticalLayout_2 = QVBoxLayout(self.page_empty)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.task = QLabel(self.page_empty)
        self.task.setObjectName(u"task")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.task.setFont(font1)
        self.task.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.task)

        self.label_3 = QLabel(self.page_empty)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_empty)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label_4)

        self.image_acc = QPushButton(self.page_empty)
        self.image_acc.setObjectName(u"image_acc")

        self.verticalLayout_2.addWidget(self.image_acc)

        self.delete_task = QPushButton(self.page_empty)
        self.delete_task.setObjectName(u"delete_task")

        self.verticalLayout_2.addWidget(self.delete_task)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_empty)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.page_info.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_18 = QVBoxLayout(self.page_info)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_info)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy13)
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"border: 0px;\n"
"background-color: transparent;\n"
"}")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 595, 606))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.task_main_info = QFrame(self.scrollAreaWidgetContents)
        self.task_main_info.setObjectName(u"task_main_info")
        self.task_main_info.setStyleSheet(u"")
        self.task_main_info.setFrameShape(QFrame.StyledPanel)
        self.task_main_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.task_main_info)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_task_name = QLabel(self.task_main_info)
        self.label_task_name.setObjectName(u"label_task_name")

        self.verticalLayout_13.addWidget(self.label_task_name)

        self.taska = QLineEdit(self.task_main_info)
        self.taska.setObjectName(u"taska")
        self.taska.setStyleSheet(u"    border: 1px solid gray;\n"
"    border-radius: 10px;")
        self.taska.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.taska)

        self.label_5 = QLabel(self.task_main_info)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)

        self.frame_edit_border = QFrame(self.task_main_info)
        self.frame_edit_border.setObjectName(u"frame_edit_border")
        self.frame_edit_border.setStyleSheet(u"QFrame{\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QWidget::hover{\n"
"border:1px solid white;\n"
"}")
        self.frame_edit_border.setFrameShape(QFrame.StyledPanel)
        self.frame_edit_border.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_edit_border)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_task_description = QLineEdit(self.frame_edit_border)
        self.lineEdit_task_description.setObjectName(u"lineEdit_task_description")
        self.lineEdit_task_description.setMinimumSize(QSize(0, 34))
        self.lineEdit_task_description.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.lineEdit_task_description)


        self.verticalLayout_13.addWidget(self.frame_edit_border)

        self.label = QLabel(self.task_main_info)
        self.label.setObjectName(u"label")

        self.verticalLayout_13.addWidget(self.label)

        self.comboBox_2 = QComboBox(self.task_main_info)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 34))
        self.comboBox_2.setEditable(True)

        self.verticalLayout_13.addWidget(self.comboBox_2)

        self.label_6 = QLabel(self.task_main_info)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_13.addWidget(self.label_6)

        self.popup = QDateEdit(self.task_main_info)
        self.popup.setObjectName(u"popup")
        self.popup.setStyleSheet(u"")
        self.popup.setCalendarPopup(True)
        self.popup.setDate(QDate(2024, 5, 30))

        self.verticalLayout_13.addWidget(self.popup)

        self.label_7 = QLabel(self.task_main_info)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)

        self.comboBox = QComboBox(self.task_main_info)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 34))
        self.comboBox.setEditable(True)

        self.verticalLayout_13.addWidget(self.comboBox)

        self.add_task = QPushButton(self.task_main_info)
        self.add_task.setObjectName(u"add_task")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        self.add_task.setFont(font2)
        self.add_task.setStyleSheet(u"    background-color: white;\n"
"    color: black;")

        self.verticalLayout_13.addWidget(self.add_task)


        self.verticalLayout_19.addWidget(self.task_main_info)

        self.task_tags_info = QFrame(self.scrollAreaWidgetContents)
        self.task_tags_info.setObjectName(u"task_tags_info")
        self.task_tags_info.setFrameShape(QFrame.StyledPanel)
        self.task_tags_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.task_tags_info)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.verticalLayout_19.addWidget(self.task_tags_info)

        self.task_date_info = QFrame(self.scrollAreaWidgetContents)
        self.task_date_info.setObjectName(u"task_date_info")
        self.task_date_info.setFrameShape(QFrame.StyledPanel)
        self.task_date_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.task_date_info)
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.verticalLayout_19.addWidget(self.task_date_info)

        self.task_tags_info_2 = QFrame(self.scrollAreaWidgetContents)
        self.task_tags_info_2.setObjectName(u"task_tags_info_2")
        self.task_tags_info_2.setFrameShape(QFrame.StyledPanel)
        self.task_tags_info_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.task_tags_info_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.verticalLayout_19.addWidget(self.task_tags_info_2)

        self.verticalSpacer_6 = QSpacerItem(17, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_info)

        self.gridLayout_7.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.info_frame, 0, 5, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 1442, 22))
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
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u0437\u0430\u0434\u0430\u0447", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u0433\u0430", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 1", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"\u041a\u0440", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 2", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 3", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043a\u0438 / \u0422\u0435\u0433\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.account_button.setText("")
        self.calendar_button.setText("")
        self.invite_button.setText("")
        self.lineEdit_add_task.setText("")
        self.lineEdit_add_task.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pushButton_tags.setText("")
        self.pushButton_assign.setText("")
        self.pushButton_data.setText("")
        self.pushButton_create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.pushButton_panel_close.setText("")
        self.label_info_week.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))
        self.comboBox_tasks_filters.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.comboBox_tasks_filters.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u04401", None))
        self.comboBox_tasks_filters.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u04402", None))

        self.comboBox_tasks_filters.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        ___qtreewidgetitem4 = self.treeWidget_overdue.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled1 = self.treeWidget_overdue.isSortingEnabled()
        self.treeWidget_overdue.setSortingEnabled(False)
        ___qtreewidgetitem5 = self.treeWidget_overdue.topLevelItem(0)
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, 3 \u0434\u043d\u044f \u043d\u0430\u0437\u0430\u0434", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem6.child(1)
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04331", None));
        self.treeWidget_overdue.setSortingEnabled(__sortingEnabled1)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_overdue), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e, <X>", None))
        ___qtreewidgetitem9 = self.treeWidget_current.headerItem()
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled2 = self.treeWidget_current.isSortingEnabled()
        self.treeWidget_current.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.treeWidget_current.topLevelItem(0)
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 1", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem14.child(0)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem14.child(1)
        ___qtreewidgetitem16.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 2", None));
        ___qtreewidgetitem17 = self.treeWidget_current.topLevelItem(1)
        ___qtreewidgetitem17.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, \u0437\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem18.child(0)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem18.child(1)
        ___qtreewidgetitem20.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 3", None));
        self.treeWidget_current.setSortingEnabled(__sortingEnabled2)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_current), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435, <X>", None))
        ___qtreewidgetitem21 = self.treeWidget_completed.headerItem()
        ___qtreewidgetitem21.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u043e\u0436\u0438\u0442\u044c", None));
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438", None));

        __sortingEnabled3 = self.treeWidget_completed.isSortingEnabled()
        self.treeWidget_completed.setSortingEnabled(False)
        ___qtreewidgetitem22 = self.treeWidget_completed.topLevelItem(0)
        ___qtreewidgetitem22.setText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a, \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem23.child(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem23.child(1)
        ___qtreewidgetitem25.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04331", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem22.child(1)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem26.child(0)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem26.child(1)
        ___qtreewidgetitem28.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04332", None));
        ___qtreewidgetitem29 = self.treeWidget_completed.topLevelItem(1)
        ___qtreewidgetitem29.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a, \u0437\u0430\u0432\u0442\u0440\u0430", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem29.child(0)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem30.child(0)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem30.child(1)
        ___qtreewidgetitem32.setText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440(?)", None));
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.treeWidget_completed.setSortingEnabled(__sortingEnabled3)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_completed), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e, <X>", None))
        self.task.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"30.05.2024", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u0443\u043c\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.image_acc.setText("")
        self.delete_task.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label_task_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.taska.setInputMask("")
        self.taska.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lineEdit_task_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438??", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433\u0438", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04331", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04332", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0432\u044f\u0437\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d", None))
        self.popup.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0438\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04331", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u04332", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 \u0442\u0435\u0433", None))
        self.add_task.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0442\u043e", None))
    # retranslateUi

