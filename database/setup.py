from database.connection import Base, engine
from database.models import TradeModel


def create_tables():
    Base.metadata.create_all(bind=engine)
