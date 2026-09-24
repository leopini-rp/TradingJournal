import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QHeaderView
)

from functools import partial

from ui.ui_main_window import Ui_MainWindow

from pages.manage_trades_page import ManageTradesPage

from database.setup import create_tables


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sets up the user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        create_tables()

        # Makes the table columns fill all available horizontal space
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.manageTradesPage = ManageTradesPage(self.ui)

        # Configures the application buttons
        self.setupButtonConnections()

    def setupButtonConnections(self):
        self.connectButton(
            self.ui.dashboardButton,
            partial(self.changePage, self.ui.dashboardPage)
        )

        self.connectButton(
            self.ui.calendarButton,
            partial(self.changePage, self.ui.calendarPage)
        )

        self.connectButton(
            self.ui.tradesButton,
            partial(self.changePage, self.ui.tradesPage)
        )

        self.connectButton(
            self.ui.manageTradesButton,
            partial(self.changePage, self.ui.manageTradesPage)
        )

    def connectButton(self, button, action):
        button.clicked.connect(action)

    def changePage(self, page):
        self.ui.mainStackedWidget.setCurrentWidget(page)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
