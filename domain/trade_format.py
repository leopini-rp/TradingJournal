import datetime

from decimal import Decimal


class Trade:
    def __init__(
            self,
            trade_date: datetime.date,
            side: str,
            size: Decimal,
            entry_price: Decimal,
            sl_price: Decimal,
            tp_price: Decimal,
            exit_price: Decimal,
            fee: Decimal,
            swap: Decimal,
            description: str,
            trade_id: int | None = None,
            created_at: datetime.datetime | None = None
    ):

        self.trade_date = trade_date
        self.side = side
        self.size = size
        self.entry_price = entry_price
        self.sl_price = sl_price
        self.tp_price = tp_price
        self.exit_price = exit_price
        self.fee = fee
        self.swap = swap
        self.description = description
        self.trade_id = trade_id
        self.created_at = created_at or datetime.datetime.now()
