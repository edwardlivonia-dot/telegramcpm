from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, DateTime, func
from database import Base

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(200))
    password: Mapped[str] = mapped_column(String(200))
    category: Mapped[str] = mapped_column(String(50)) # free, premium
    status: Mapped[str] = mapped_column(String(20), default="available")
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
