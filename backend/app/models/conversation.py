from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True)

    buyer_id: Mapped[int] = mapped_column(
        ForeignKey("buyers.id")
    )

    buyer = relationship(
        "Buyer",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation"
    )
