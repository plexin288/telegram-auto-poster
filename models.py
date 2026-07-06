from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime
)

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    type = Column(
        String(20),
        nullable=False
    )

    file_path = Column(
        String(255),
        nullable=True
    )

    caption = Column(
        Text,
        nullable=True
    )

    scheduled_at = Column(
        DateTime,
        nullable=False
    )

    is_sent = Column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
