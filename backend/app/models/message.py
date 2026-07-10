from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Message(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id")
    )

    sender: Mapped[str]

    content: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )
