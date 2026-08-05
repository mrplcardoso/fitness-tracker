from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import DATA_DIR, DATABASE_FILE

DATA_DIR.mkdir(exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(DATABASE_URL, echo=False)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine)

def create_database():
    import src.models
    Base.metadata.create_all(bind=engine)