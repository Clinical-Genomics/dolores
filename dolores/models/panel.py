from dolores.db.base_class import Base
from dolores.models.customer import Customer
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Panel(Base):

    abbrev = Column(String(32), unique=True)
    current_version = Column(Float, nullable=False)
    customer_id = Column(ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
    customer = relationship(Customer, backref="panels")
    date = Column(DateTime, nullable=False)
    gene_count = Column(Integer)
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __str__(self):
        return f"{self.abbrev} ({self.current_version})"
