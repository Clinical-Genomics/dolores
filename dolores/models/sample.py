from datetime import datetime

from dolores.constants import SEX_OPTIONS
from dolores.db.base_class import Base
from dolores.models.application import ApplicationVersion
from dolores.models.delivery import Delivery
from dolores.models.mixin import PriorityMixin
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

flowcell_sample = Table(
    "flowcell_sample",
    Base.metadata,
    Column("flowcell_id", Integer, ForeignKey("flowcell.id"), nullable=False),
    Column("sample_id", Integer, ForeignKey("sample.id"), nullable=False),
    UniqueConstraint("flowcell_id", "sample_id", name="_flowcell_sample_uc"),
)


class Sample(Base, PriorityMixin):
    id = Column(Integer, primary_key=True)
    application_version_id = Column(ForeignKey("application_version.id"), nullable=False)
    application_version = relationship(ApplicationVersion, foreign_keys=[application_version_id])
    capture_kit = Column(String(64))
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    customer_id = Column(ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
    customer = relationship("Customer", foreign_keys=[customer_id])
    delivered_at = Column(DateTime)
    deliveries = relationship(Delivery, backref="sample")
    downsampled_to = Column(BigInteger)
    from_sample = Column(String(128))
    internal_id = Column(String(32), nullable=False, unique=True)
    invoice_id = Column(ForeignKey("invoice.id"))
    invoiced_at = Column(DateTime)  # DEPRECATED
    is_external = Column(Boolean, default=False)  # DEPRECATED
    is_tumour = Column(Boolean, default=False)
    loqusdb_id = Column(String(64))
    name = Column(String(128), nullable=False)
    no_invoice = Column(Boolean, default=False)
    order = Column(String(64))
    ordered_at = Column(DateTime, nullable=False)
    organism_id = Column(ForeignKey("organism.id"))
    organism = relationship("Organism", foreign_keys=[organism_id])
    prepared_at = Column(DateTime)
    priority = Column(Integer, default=1, nullable=False)
    reads = Column(BigInteger, default=0)
    received_at = Column(DateTime)
    reference_genome = Column(String(255))
    sequence_start = Column(DateTime)
    sequenced_at = Column(DateTime)
    sex = Column(Enum(*SEX_OPTIONS), nullable=False)
    ticket_number = Column(Integer)
    time_point = Column(Integer)

    def __str__(self) -> str:
        return f"{self.internal_id} ({self.name})"

    @property
    def state(self) -> str:
        """Get the current sample state."""
        if self.delivered_at:
            return f"Delivered {self.delivered_at.date()}"
        elif self.sequenced_at:
            return f"Sequenced {self.sequenced_at.date()}"
        elif self.sequence_start:
            return f"Sequencing {self.sequence_start.date()}"
        elif self.received_at:
            return f"Received {self.received_at.date()}"
        else:
            return f"Ordered {self.ordered_at.date()}"

    def to_dict(self, links: bool = False, flowcells: bool = False) -> dict:
        """Represent as dictionary"""
        data = super(Sample, self).to_dict()
        data["priority"] = self.priority_human
        data["customer"] = self.customer.to_dict()
        data["application_version"] = self.application_version.to_dict()
        data["application"] = self.application_version.application.to_dict()
        if links:
            data["links"] = [link_obj.to_dict(family=True, parents=True) for link_obj in self.links]
        if flowcells:
            data["flowcells"] = [flowcell_obj.to_dict() for flowcell_obj in self.flowcells]
        return data
