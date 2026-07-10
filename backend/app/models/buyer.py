from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Buyer(Base):
    __tablename__ = "buyers"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    display_name: Mapped[str] = mapped_column(
        String(100)
    )

    conversations = relationship(
        "Conversation",
        back_populates="buyer"
    )
