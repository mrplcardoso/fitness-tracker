from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Food(Base):

    __tablename__ = "foods"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    serving: Mapped[int] = mapped_column(Integer)
    calories: Mapped[float] = mapped_column(Float)
    carbohydrates: Mapped[float] = mapped_column(Float)
    protein: Mapped[float] = mapped_column(Float)
    fat: Mapped[float] = mapped_column(Float)