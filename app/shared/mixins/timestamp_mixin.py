from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimestampMixin:
    """Mixin que adiciona created_at e updated_at a qualquer model."""

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now(),
        nullable=False,
    )
