from datetime import datetime

from dolores.db.base_class import Base
from dolores.models.customer import Customer
from dolores.models.pool import Pool
from dolores.models.sample import Sample
from sqlalchemy import BLOB, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship


class Invoice(Base):
    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey("customer.id"), nullable=False)
    customer = relationship(Customer, foreign_keys=[customer_id])
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
    invoiced_at = Column(DateTime)
    comment = Column(Text)
    discount = Column(Integer, default=0)
    excel_kth = Column(BLOB)
    excel_ki = Column(BLOB)
    price = Column(Integer)
    record_type = Column(Text)

    samples = relationship(Sample, backref="invoice")
    pools = relationship(Pool, backref="invoice")

    def __str__(self):
        return f"{self.customer_id} ({self.invoiced_at})"
