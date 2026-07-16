from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, Boolean
from database import Base

class AccessKey(Base):
    __tablename__ = "access_keys"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    key: Mapped[str] = mapped_column(String(50), unique=True)
    type: Mapped[str] = mapped_column(String(20)) # vip, premium_logs, premium_bot
    is_used: Mapped[bool] = mapped_column(Boolean, default=False)
    used_by: Mapped[int] = mapped_column(BigInteger, nullable=True)
