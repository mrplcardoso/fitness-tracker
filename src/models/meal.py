from datetime import date
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from src.database import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .meal_item import MealItem

class Meal(Base):

    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date)
    name: Mapped[str] = mapped_column(String(50))
    items: Mapped[list["MealItem"]] = relationship(back_populates="meal",
                                                   cascade="all, delete-orphan")