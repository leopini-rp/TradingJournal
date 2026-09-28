from ui.ui_main_window import Ui_MainWindow

from domain.trade_format import Trade

from PySide6.QtCore import QDate, Qt, QEvent, QObject

from PySide6.QtWidgets import (
    QTableWidgetItem, QApplication, QWidget, QStyledItemDelegate, QDateEdit
)

from repository.trade_repository import (
    save_trade_to_db, get_trades
)


class DateDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QDateEdit(parent)

        editor.setDisplayFormat("yyyy-MM-dd")
        editor.setCalendarPopup(True)

        return editor

    def setEditorData(self, editor, index):
        dateText = index.data()

        date = QDate.fromString(dateText, "yyyy-MM-dd")

        editor.setDate(date)

    def setModelData(self, editor, model, index):
        date = editor.date()

        model.setData(
            index,
            date.toString("yyyy-MM-dd")
        )


class ManageTradesPage(QObject):
    def __init__(self, ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui

        QApplication.instance().installEventFilter(self)

        self.setCurrentDate(self.ui.dateInput)

        self.configureUi()

        self.addButtonValidation()

        self.dbTradesToTable()

    def configureUi(self):
        self.connectButton(
            self.ui.addTradeButton,
            self.saveTrade
        )

        self.connectButton(
            self.ui.editbutton,
            self.editItem
        )

        self.ui.editbutton.setEnabled(False)
        self.ui.removeButton.setEnabled(False)

        self.ui.tableWidget.itemSelectionChanged.connect(
            self.validateTableButtons
        )

        dateDelegate = DateDelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegateForColumn(0, dateDelegate)

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

    def validateTableButtons(self):
        # Check if there's a table item selected
        selectionCheck = bool(self.ui.tableWidget.selectedItems())

        buttons = (
            self.ui.editbutton,
            self.ui.removeButton
        )

        for button in buttons:
            button.setEnabled(selectionCheck)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:

            if not isinstance(obj, QWidget):
                return super().eventFilter(obj, event)

            table = self.ui.tableWidget

            if obj == table.viewport():
                item = table.itemAt(event.position().toPoint())

                if item is None:
                    table.clearSelection()

            else:
                buttons = (
                    self.ui.editbutton,
                    self.ui.removeButton
                )

                clickedButton = False

                for button in buttons:
                    if obj == button or button.isAncestorOf(obj):
                        clickedButton = True
                        break

                if not clickedButton:
                    table.clearSelection()

        return super().eventFilter(obj, event)

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

        descriptionColumn = "✓" if trade.description.strip() else "-"

        values = (
            trade.trade_date,
            trade.side,
            trade.size,
            trade.entry_price,
            trade.sl_price,
            trade.tp_price,
            trade.exit_price,
            trade.fee,
            trade.swap,
            descriptionColumn
        )

        for column, value in enumerate(values):
            item = QTableWidgetItem(str(value))
            self.ui.tableWidget.setItem(row, column, item)

        # Stores the trade ID in UserRole
        dateItem = QTableWidgetItem(str(trade.trade_date))
        dateItem.setData(Qt.UserRole, trade.trade_id)

        self.ui.tableWidget.setItem(row, 0, dateItem)

    def editItem(self):
        selectedItem = self.ui.tableWidget.currentItem()
        self.editingItem = selectedItem

        self.editingId = self.getSelectedItemId()

        self.originalValue = selectedItem.text()

        self.ui.tableWidget.editItem(selectedItem)

    def getSelectedItemId(self):
        row = self.ui.tableWidget.currentRow()
        item = self.ui.tableWidget.item(row, 0)

        return item.data(Qt.UserRole)

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
