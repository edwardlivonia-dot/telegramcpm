from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, Boolean, Float
from database import Base

class RedeemCode(Base):
    __tablename__ = "redeem_codes"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    code: Mapped[str] = mapped_column(String(50), unique=True)
    amount: Mapped[float] = mapped_column(Float)
    type: Mapped[str] = mapped_column(String(20)) # wallet or limit
    is_used: Mapped[bool] = mapped_column(Boolean, default=False)
    used_by: Mapped[int] = mapped_column(BigInteger, nullable=True)
