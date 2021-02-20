from datetime import datetime

from dolores.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text


class Organism(Base):
    id = Column(Integer, primary_key=True)
    internal_id = Column(String(32), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
    reference_genome = Column(String(255))
    verified = Column(Boolean, default=False)
    comment = Column(Text)

    def __str__(self) -> str:
        return f"{self.internal_id} ({self.name})"
