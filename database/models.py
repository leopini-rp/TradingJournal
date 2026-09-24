import datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class TradeModel(Base):
    __tablename__ = "trades"

    # Mapped defines the Python type; mapped_column defines the database column
    trade_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    trade_date: Mapped[datetime.date] = mapped_column(
        Date,
        nullable=False,
        index=True
    )

    side: Mapped[str] = mapped_column(
        String(4),
        nullable=False
    )

    size: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    entry_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    sl_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    tp_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    exit_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    fee: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        default=Decimal("0.00")
    )

    swap: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        default=Decimal("0.00")
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default=""
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )
