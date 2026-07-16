from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, Float, Date, String, func
from database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=True)
    wallet_balance: Mapped[float] = mapped_column(Float, default=0.0)
    orders_today: Mapped[int] = mapped_column(Integer, default=0)
    last_order_date: Mapped[Date] = mapped_column(Date, default=func.current_date())
    extra_limits_bought: Mapped[int] = mapped_column(Integer, default=0)
