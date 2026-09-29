from database.connection import SessionLocal
from database.models import TradeModel
from domain.trade_format import Trade


from sqlalchemy import select


def save_trade_to_db(trade):
    trade_model = TradeModel(
        trade_date=trade.trade_date,
        side=trade.side,
        size=trade.size,
        entry_price=trade.entry_price,
        sl_price=trade.sl_price,
        tp_price=trade.tp_price,
        exit_price=trade.exit_price,
        fee=trade.fee,
        swap=trade.swap,
        description=trade.description
    )

    session = SessionLocal()

    session.add(trade_model)
    session.commit()
    session.refresh(trade_model)

    session.close()

    return trade_model


def get_trades():
    session = SessionLocal()

    stmt = select(TradeModel)
    result = session.execute(stmt)

    trades = result.scalars().all()

    return model_to_trade(trades)


def model_to_trade(trades):
    trade_list = []

    for trade_model in trades:
        trade = Trade(
            trade_date=trade_model.trade_date,
            side=trade_model.side,
            size=trade_model.size,
            entry_price=trade_model.entry_price,
            sl_price=trade_model.sl_price,
            tp_price=trade_model.tp_price,
            exit_price=trade_model.exit_price,
            fee=trade_model.fee,
            swap=trade_model.swap,
            description=trade_model.description,
            trade_id=trade_model.trade_id,
            created_at=trade_model.created_at
        )

        trade_list.append(trade)

    return trade_list


def get_db_item(trade_id, field):
    session = SessionLocal()

    trade = session.get(TradeModel, trade_id)

    value = getattr(trade, field)

    session.close()

    return value
