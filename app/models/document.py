from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String, ForeignKey
from app.db.database import Base
from datetime import datetime
from sqlalchemy import DateTime, func

class Document(Base):
    __tablename__ = "documents"

    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    filename : Mapped[str] = mapped_column(
        String,
        nullable = False
    )

    owner_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable = False
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    owner = relationship("User",back_populates="documents")
    