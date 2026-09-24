from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / "trading_journal.sqlite3"

DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine)
