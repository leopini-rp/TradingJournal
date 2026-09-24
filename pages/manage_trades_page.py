from ui.ui_main_window import Ui_MainWindow

from domain.trade_format import Trade

from PySide6.QtCore import QDate

from PySide6.QtWidgets import QTableWidgetItem

from repository.trade_repository import (
    save_trade_to_db, get_trades
)


class ManageTradesPage:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.setCurrentDate(self.ui.dateInput)

        self.setupButtonConnections()

        self.addButtonValidation()

        self.dbTradesToTable()

    def setupButtonConnections(self):
        self.connectButton(
            self.ui.addTradeButton,
            self.saveTrade
        )

    def connectButton(self, button, action):
        button.clicked.connect(action)

    def addButtonValidation(self):
        self.requiredTradeInputs = (
            self.ui.sizeInput,
            self.ui.entryPriceInput,
            self.ui.slPriceInput,
            self.ui.tpPriceInput,
            self.ui.exitPriceInput
        )

        for inputField in self.requiredTradeInputs:
            inputField.valueChanged.connect(self.validateAddButton)

        self.validateAddButton()

    def validateAddButton(self, *_):
        isValid = all(
            inputField.value() > 0
            for inputField in self.requiredTradeInputs
        )

        self.ui.addTradeButton.setEnabled(isValid)

# region Input Format

    def setCurrentDate(self, dateInput):
        dateInput.setDate(QDate.currentDate())

# endregion

# region data functions

    def createTradeFromInputs(self):
        trade = Trade(
            trade_date=self.ui.dateInput.date().toPython(),
            side=self.ui.sideInput.currentText(),
            size=self.ui.sizeInput.value(),
            entry_price=self.ui.entryPriceInput.value(),
            sl_price=self.ui.slPriceInput.value(),
            tp_price=self.ui.tpPriceInput.value(),
            exit_price=self.ui.exitPriceInput.value(),
            fee=self.ui.feeInput.value(),
            swap=self.ui.swapInput.value(),
            description=self.ui.descriptionInput.toPlainText()
        )

        return trade

    def saveTrade(self):
        trade = self.createTradeFromInputs()

        # trade_repository func
        save_trade_to_db(trade)

        self.addTradeToTable(trade)

    def dbTradesToTable(self):
        # trade_repository func
        tradesList = get_trades()

        for trade in tradesList:
            self.addTradeToTable(trade)

    def addTradeToTable(self, trade):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        values = (
            trade.trade_date,
            trade.side,
            trade.size,
            trade.entry_price,
            trade.sl_price,
            trade.tp_price,
            trade.exit_price,
            trade.fee,
            trade.swap
        )

        for column, value in enumerate(values):
            item = QTableWidgetItem(str(value))
            self.ui.tableWidget.setItem(row, column, item)
# endregion

        # self.trade_date = trade_date
        # self.side = side
        # self.size = size
        # self.entry_price = entry_price
        # self.sl_price = sl_price
        # self.tp_price = tp_price
        # self.exit_price = exit_price
        # self.fee = fee
        # self.swap = swap
        # self.description = description
        # self.trade_id = trade_id
        # self.created_at = created_at
