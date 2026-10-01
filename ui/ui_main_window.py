# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 591)
        MainWindow.setMinimumSize(QSize(1100, 0))
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebarFrame.sizePolicy().hasHeightForWidth())
        self.sidebarFrame.setSizePolicy(sizePolicy)
        self.sidebarFrame.setAutoFillBackground(False)
        self.sidebarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboardButton = QPushButton(self.sidebarFrame)
        self.dashboardButton.setObjectName(u"dashboardButton")

        self.verticalLayout.addWidget(self.dashboardButton)

        self.calendarButton = QPushButton(self.sidebarFrame)
        self.calendarButton.setObjectName(u"calendarButton")

        self.verticalLayout.addWidget(self.calendarButton)

        self.tradesButton = QPushButton(self.sidebarFrame)
        self.tradesButton.setObjectName(u"tradesButton")

        self.verticalLayout.addWidget(self.tradesButton)

        self.manageTradesButton = QPushButton(self.sidebarFrame)
        self.manageTradesButton.setObjectName(u"manageTradesButton")

        self.verticalLayout.addWidget(self.manageTradesButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.mainStackedWidget.addWidget(self.dashboardPage)
        self.calendarPage = QWidget()
        self.calendarPage.setObjectName(u"calendarPage")
        self.mainStackedWidget.addWidget(self.calendarPage)
        self.tradesPage = QWidget()
        self.tradesPage.setObjectName(u"tradesPage")
        self.mainStackedWidget.addWidget(self.tradesPage)
        self.manageTradesPage = QWidget()
        self.manageTradesPage.setObjectName(u"manageTradesPage")
        self.verticalLayout_2 = QVBoxLayout(self.manageTradesPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tradesFrame = QFrame(self.manageTradesPage)
        self.tradesFrame.setObjectName(u"tradesFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tradesFrame.sizePolicy().hasHeightForWidth())
        self.tradesFrame.setSizePolicy(sizePolicy1)
        self.tradesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tradesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.tradesFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.tradesFrame)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.entryPriceInput = QDoubleSpinBox(self.tradesFrame)
        self.entryPriceInput.setObjectName(u"entryPriceInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.entryPriceInput.sizePolicy().hasHeightForWidth())
        self.entryPriceInput.setSizePolicy(sizePolicy3)
        self.entryPriceInput.setMinimumSize(QSize(85, 25))
        self.entryPriceInput.setMaximumSize(QSize(16777215, 25))
        self.entryPriceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.entryPriceInput.setMaximum(999999.989999999990687)

        self.gridLayout_3.addWidget(self.entryPriceInput, 1, 3, 1, 1)

        self.sizeLabel = QLabel(self.tradesFrame)
        self.sizeLabel.setObjectName(u"sizeLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sizeLabel.sizePolicy().hasHeightForWidth())
        self.sizeLabel.setSizePolicy(sizePolicy4)
        self.sizeLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.sizeLabel, 0, 2, 1, 1)

        self.tpPriceLabel = QLabel(self.tradesFrame)
        self.tpPriceLabel.setObjectName(u"tpPriceLabel")
        sizePolicy4.setHeightForWidth(self.tpPriceLabel.sizePolicy().hasHeightForWidth())
        self.tpPriceLabel.setSizePolicy(sizePolicy4)
        self.tpPriceLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.tpPriceLabel, 0, 5, 1, 1)

        self.slPriceLabel = QLabel(self.tradesFrame)
        self.slPriceLabel.setObjectName(u"slPriceLabel")
        sizePolicy4.setHeightForWidth(self.slPriceLabel.sizePolicy().hasHeightForWidth())
        self.slPriceLabel.setSizePolicy(sizePolicy4)
        self.slPriceLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.slPriceLabel, 0, 4, 1, 1)

        self.feeLabel = QLabel(self.tradesFrame)
        self.feeLabel.setObjectName(u"feeLabel")
        sizePolicy4.setHeightForWidth(self.feeLabel.sizePolicy().hasHeightForWidth())
        self.feeLabel.setSizePolicy(sizePolicy4)
        self.feeLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.feeLabel, 0, 7, 1, 1)

        self.exitPriceInput = QDoubleSpinBox(self.tradesFrame)
        self.exitPriceInput.setObjectName(u"exitPriceInput")
        sizePolicy3.setHeightForWidth(self.exitPriceInput.sizePolicy().hasHeightForWidth())
        self.exitPriceInput.setSizePolicy(sizePolicy3)
        self.exitPriceInput.setMinimumSize(QSize(85, 25))
        self.exitPriceInput.setMaximumSize(QSize(16777215, 25))
        self.exitPriceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.exitPriceInput.setMaximum(999999.989999999990687)

        self.gridLayout_3.addWidget(self.exitPriceInput, 1, 6, 1, 1)

        self.feeInput = QDoubleSpinBox(self.tradesFrame)
        self.feeInput.setObjectName(u"feeInput")
        sizePolicy3.setHeightForWidth(self.feeInput.sizePolicy().hasHeightForWidth())
        self.feeInput.setSizePolicy(sizePolicy3)
        self.feeInput.setMinimumSize(QSize(85, 25))
        self.feeInput.setMaximumSize(QSize(16777215, 25))
        self.feeInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.feeInput.setMaximum(999999.989999999990687)

        self.gridLayout_3.addWidget(self.feeInput, 1, 7, 1, 1)

        self.exitPriceLabel = QLabel(self.tradesFrame)
        self.exitPriceLabel.setObjectName(u"exitPriceLabel")
        sizePolicy4.setHeightForWidth(self.exitPriceLabel.sizePolicy().hasHeightForWidth())
        self.exitPriceLabel.setSizePolicy(sizePolicy4)
        self.exitPriceLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.exitPriceLabel, 0, 6, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.swapInput = QDoubleSpinBox(self.tradesFrame)
        self.swapInput.setObjectName(u"swapInput")
        sizePolicy3.setHeightForWidth(self.swapInput.sizePolicy().hasHeightForWidth())
        self.swapInput.setSizePolicy(sizePolicy3)
        self.swapInput.setMinimumSize(QSize(85, 25))
        self.swapInput.setMaximumSize(QSize(16777215, 25))
        self.swapInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.swapInput.setMaximum(999999.989999999990687)

        self.gridLayout_3.addWidget(self.swapInput, 1, 8, 1, 1)

        self.slPriceInput = QDoubleSpinBox(self.tradesFrame)
        self.slPriceInput.setObjectName(u"slPriceInput")
        sizePolicy3.setHeightForWidth(self.slPriceInput.sizePolicy().hasHeightForWidth())
        self.slPriceInput.setSizePolicy(sizePolicy3)
        self.slPriceInput.setMinimumSize(QSize(85, 25))
        self.slPriceInput.setMaximumSize(QSize(16777215, 25))
        self.slPriceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.slPriceInput.setMaximum(999999.989999999990687)

        self.gridLayout_3.addWidget(self.slPriceInput, 1, 4, 1, 1)

        self.sideInput = QComboBox(self.tradesFrame)
        self.sideInput.addItem("")
        self.sideInput.addItem("")
        self.sideInput.setObjectName(u"sideInput")
        sizePolicy3.setHeightForWidth(self.sideInput.sizePolicy().hasHeightForWidth())
        self.sideInput.setSizePolicy(sizePolicy3)
        self.sideInput.setMinimumSize(QSize(85, 25))
        self.sideInput.setMaximumSize(QSize(16777215, 25))
        self.sideInput.setEditable(False)
        self.sideInput.setMaxVisibleItems(12)

        self.gridLayout_3.addWidget(self.sideInput, 1, 1, 1, 1)

        self.dateLabel = QLabel(self.tradesFrame)
        self.dateLabel.setObjectName(u"dateLabel")
        sizePolicy4.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setBold(False)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet(u"padding-left: 1px;")
        self.dateLabel.setMargin(0)

        self.gridLayout_3.addWidget(self.dateLabel, 0, 0, 1, 1)

        self.entryPriceLabel = QLabel(self.tradesFrame)
        self.entryPriceLabel.setObjectName(u"entryPriceLabel")
        sizePolicy4.setHeightForWidth(self.entryPriceLabel.sizePolicy().hasHeightForWidth())
        self.entryPriceLabel.setSizePolicy(sizePolicy4)
        self.entryPriceLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.entryPriceLabel, 0, 3, 1, 1)

        self.sizeInput = QDoubleSpinBox(self.tradesFrame)
        self.sizeInput.setObjectName(u"sizeInput")
        sizePolicy3.setHeightForWidth(self.sizeInput.sizePolicy().hasHeightForWidth())
        self.sizeInput.setSizePolicy(sizePolicy3)
        self.sizeInput.setMinimumSize(QSize(85, 25))
        self.sizeInput.setMaximumSize(QSize(16777215, 25))
        self.sizeInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sizeInput.setMaximum(999.990000000000009)

        self.gridLayout_3.addWidget(self.sizeInput, 1, 2, 1, 1)

        self.tpPriceInput = QDoubleSpinBox(self.tradesFrame)
        self.tpPriceInput.setObjectName(u"tpPriceInput")
        sizePolicy3.setHeightForWidth(self.tpPriceInput.sizePolicy().hasHeightForWidth())
        self.tpPriceInput.setSizePolicy(sizePolicy3)
        self.tpPriceInput.setMinimumSize(QSize(85, 25))
        self.tpPriceInput.setMaximumSize(QSize(16777215, 25))
        self.tpPriceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tpPriceInput.setMaximum(999999.989999999990687)

        self.gridLayout_3.addWidget(self.tpPriceInput, 1, 5, 1, 1)

        self.swapLabel = QLabel(self.tradesFrame)
        self.swapLabel.setObjectName(u"swapLabel")
        sizePolicy4.setHeightForWidth(self.swapLabel.sizePolicy().hasHeightForWidth())
        self.swapLabel.setSizePolicy(sizePolicy4)
        self.swapLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.swapLabel, 0, 8, 1, 1)

        self.dateInput = QDateEdit(self.tradesFrame)
        self.dateInput.setObjectName(u"dateInput")
        sizePolicy3.setHeightForWidth(self.dateInput.sizePolicy().hasHeightForWidth())
        self.dateInput.setSizePolicy(sizePolicy3)
        self.dateInput.setMinimumSize(QSize(85, 25))
        self.dateInput.setMaximumSize(QSize(16777215, 25))
        self.dateInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateInput.setProperty(u"showGroupSeparator", False)
        self.dateInput.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.dateInput.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateInput, 1, 0, 1, 1)

        self.descriptionLabel = QLabel(self.tradesFrame)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        sizePolicy4.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.descriptionLabel, 4, 0, 1, 1)

        self.sideLabel = QLabel(self.tradesFrame)
        self.sideLabel.setObjectName(u"sideLabel")
        sizePolicy4.setHeightForWidth(self.sideLabel.sizePolicy().hasHeightForWidth())
        self.sideLabel.setSizePolicy(sizePolicy4)
        self.sideLabel.setStyleSheet(u"padding-left: 1px;")

        self.gridLayout_3.addWidget(self.sideLabel, 0, 1, 1, 1)

        self.descriptionInput = QTextEdit(self.tradesFrame)
        self.descriptionInput.setObjectName(u"descriptionInput")
        sizePolicy3.setHeightForWidth(self.descriptionInput.sizePolicy().hasHeightForWidth())
        self.descriptionInput.setSizePolicy(sizePolicy3)
        self.descriptionInput.setMinimumSize(QSize(0, 150))
        self.descriptionInput.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_3.addWidget(self.descriptionInput, 5, 0, 1, 9)

        self.addTradeButton = QPushButton(self.tradesFrame)
        self.addTradeButton.setObjectName(u"addTradeButton")

        self.gridLayout_3.addWidget(self.addTradeButton, 6, 7, 1, 2)

        self.label = QLabel(self.tradesFrame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setMargin(6)

        self.gridLayout_3.addWidget(self.label, 6, 0, 1, 1)

        self.gridLayout_3.setRowStretch(6, 1)

        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.editbutton = QPushButton(self.tradesFrame)
        self.editbutton.setObjectName(u"editbutton")

        self.horizontalLayout_2.addWidget(self.editbutton)

        self.removeButton = QPushButton(self.tradesFrame)
        self.removeButton.setObjectName(u"removeButton")

        self.horizontalLayout_2.addWidget(self.removeButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.tradesFrame)

        self.mainStackedWidget.addWidget(self.manageTradesPage)

        self.horizontalLayout.addWidget(self.mainStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.dateInput, self.sideInput)
        QWidget.setTabOrder(self.sideInput, self.sizeInput)
        QWidget.setTabOrder(self.sizeInput, self.entryPriceInput)
        QWidget.setTabOrder(self.entryPriceInput, self.slPriceInput)
        QWidget.setTabOrder(self.slPriceInput, self.tpPriceInput)
        QWidget.setTabOrder(self.tpPriceInput, self.exitPriceInput)
        QWidget.setTabOrder(self.exitPriceInput, self.feeInput)
        QWidget.setTabOrder(self.feeInput, self.swapInput)
        QWidget.setTabOrder(self.swapInput, self.descriptionInput)
        QWidget.setTabOrder(self.descriptionInput, self.addTradeButton)
        QWidget.setTabOrder(self.addTradeButton, self.calendarButton)
        QWidget.setTabOrder(self.calendarButton, self.dashboardButton)
        QWidget.setTabOrder(self.dashboardButton, self.manageTradesButton)

        self.retranslateUi(MainWindow)

        self.mainStackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.tradesButton.setText(QCoreApplication.translate("MainWindow", u"Trades", None))
        self.manageTradesButton.setText(QCoreApplication.translate("MainWindow", u"Manage Trades", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Side", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Entry Price", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SL Price", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TP Price", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Exit Price", None))
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Fee", None))
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.tpPriceLabel.setText(QCoreApplication.translate("MainWindow", u"TP Price", None))
        self.slPriceLabel.setText(QCoreApplication.translate("MainWindow", u"SL Price", None))
        self.feeLabel.setText(QCoreApplication.translate("MainWindow", u"Fee", None))
        self.exitPriceLabel.setText(QCoreApplication.translate("MainWindow", u"Exit Price", None))
        self.sideInput.setItemText(0, QCoreApplication.translate("MainWindow", u"BUY", None))
        self.sideInput.setItemText(1, QCoreApplication.translate("MainWindow", u"SELL", None))

        self.sideInput.setCurrentText("")
        self.sideInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BUY or SELL", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.entryPriceLabel.setText(QCoreApplication.translate("MainWindow", u"Entry Price", None))
        self.swapLabel.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        self.dateInput.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.sideLabel.setText(QCoreApplication.translate("MainWindow", u"Side", None))
        self.addTradeButton.setText(QCoreApplication.translate("MainWindow", u"Add Trade", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"(0/500)", None))
        self.editbutton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

