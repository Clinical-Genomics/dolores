from datetime import datetime
from typing import List

from dolores.constants import CASE_ACTIONS, STATUS_OPTIONS, DataDelivery, Pipeline
from dolores.db.base_class import Base
from dolores.models.analysis import Analysis
from dolores.models.customer import Customer
from dolores.models.mixin import PriorityMixin
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import relationship


class Family(Base, PriorityMixin):
    __table_args__ = (UniqueConstraint("customer_id", "name", name="_customer_name_uc"),)

    action = Column(Enum(*CASE_ACTIONS))
    analyses = relationship(Analysis, backref="family", order_by="-Analysis.completed_at")
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    customer_id = Column(ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
    customer = relationship(Customer, foreign_keys=[customer_id])
    data_analysis = Column(Enum(*list(Pipeline)))
    data_delivery = Column(Enum(*list(DataDelivery)))
    id = Column(Integer, primary_key=True)
    internal_id = Column(String(32), unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    ordered_at = Column(DateTime, default=datetime.now)
    _panels = Column(Text)
    priority = Column(Integer, default=1, nullable=False)

    def __str__(self) -> str:
        return f"{self.internal_id} ({self.name})"

    @property
    def panels(self) -> List[str]:
        """Return a list of panels."""
        return self._panels.split(",") if self._panels else []

    @panels.setter
    def panels(self, panel_list: List[str]):
        self._panels = ",".join(panel_list) if panel_list else None


class FamilySample(Base):
    __table_args__ = (UniqueConstraint("family_id", "sample_id", name="_family_sample_uc"),)

    id = Column(Integer, primary_key=True)
    family_id = Column(ForeignKey("family.id", ondelete="CASCADE"), nullable=False)
    sample_id = Column(ForeignKey("sample.id", ondelete="CASCADE"), nullable=False)
    status = Column(Enum(*STATUS_OPTIONS), default="unknown", nullable=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    mother_id = Column(ForeignKey("sample.id"))
    father_id = Column(ForeignKey("sample.id"))

    family = relationship("Family", backref="links")
    sample = relationship("Sample", foreign_keys=[sample_id], backref="links")
    mother = relationship("Sample", foreign_keys=[mother_id], backref="mother_links")
    father = relationship("Sample", foreign_keys=[father_id], backref="father_links")

    def __str__(self) -> str:
        return f"{self.family.internal_id} | {self.sample.internal_id}"
