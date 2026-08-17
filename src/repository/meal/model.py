from datetime import date
from sqlalchemy import String, Date, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from src.database import Base

from src.repository.food.model import Food

class Item(Base):

    __tablename__ = "meal_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    meal_id: Mapped[int] = mapped_column(ForeignKey("meals.id"))
    food_id: Mapped[int] = mapped_column(ForeignKey("foods.id"))
    grams: Mapped[float] = mapped_column(Float)

    meal: Mapped["Meal"] = relationship(back_populates="items")
    food: Mapped["Food"] = relationship(lazy="joined")
    

class Meal(Base):

    __tablename__ = "meals"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date)
    name: Mapped[str] = mapped_column(String(50))
    items: Mapped[list["Item"]] = relationship(back_populates="meal",
                                                   cascade="all, delete-orphan")