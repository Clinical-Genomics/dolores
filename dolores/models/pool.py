from datetime import datetime

from dolores.db.base_class import Base
from dolores.models.application import ApplicationVersion
from dolores.models.customer import Customer
from dolores.models.delivery import Delivery
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship


class Pool(Base):
    __table_args__ = (UniqueConstraint("order", "name", name="_order_name_uc"),)

    application_version_id = Column(ForeignKey("application_version.id"), nullable=False)
    application_version = relationship(ApplicationVersion, foreign_keys=[application_version_id])
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    customer_id = Column(ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
    customer = relationship(Customer, foreign_keys=[customer_id])
    data_analysis = Column(String(16))
    delivered_at = Column(DateTime)
    deliveries = relationship(Delivery, backref="pool")
    id = Column(Integer, primary_key=True)
    invoice_id = Column(ForeignKey("invoice.id"))
    invoiced_at = Column(DateTime)  # DEPRECATED
    lims_project = Column(Text)
    name = Column(String(32), nullable=False)
    no_invoice = Column(Boolean, default=False)
    order = Column(String(64), nullable=False)
    ordered_at = Column(DateTime, nullable=False)
    reads = Column(BigInteger, default=0)
    received_at = Column(DateTime)
    sequenced_at = Column(DateTime)
    ticket_number = Column(Integer)
