from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .food import Food
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .meal import Meal

from src.database import Base

class MealItem(Base):

    __tablename__ = "meal_items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    meal_id: Mapped[int] = mapped_column(ForeignKey("meals.id"))
    food_id: Mapped[int] = mapped_column(ForeignKey("foods.id"))
    grams: Mapped[float] = mapped_column(Float)
    meal: Mapped["Meal"] = relationship(back_populates="items")
    food: Mapped["Food"] = relationship(lazy="joined")