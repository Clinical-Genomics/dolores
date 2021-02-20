from dolores.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Customer(Base):
    id = Column(Integer, primary_key=True)
    internal_id = Column(String(32), unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    priority = Column(Enum("diagnostic", "research"))
    scout_access = Column(Boolean, nullable=False, default=False)
    loqus_upload = Column(Boolean, nullable=False, default=False)
    return_samples = Column(Boolean, nullable=False, default=False)

    agreement_date = Column(DateTime)
    agreement_registration = Column(String(32))
    project_account_ki = Column(String(32))
    project_account_kth = Column(String(32))
    organisation_number = Column(String(32))
    invoice_address = Column(Text, nullable=False)
    invoice_reference = Column(String(32), nullable=False)
    uppmax_account = Column(String(32))
    comment = Column(Text)

    primary_contact_id = Column(ForeignKey("user.id"))
    primary_contact = relationship("User", foreign_keys=[primary_contact_id])
    delivery_contact_id = Column(ForeignKey("user.id"))
    delivery_contact = relationship("User", foreign_keys=[delivery_contact_id])
    invoice_contact_id = Column(ForeignKey("user.id"))
    invoice_contact = relationship("User", foreign_keys=[invoice_contact_id])
    customer_group_id = Column(ForeignKey("customer_group.id"), nullable=False)

    def __str__(self) -> str:
        return f"{self.internal_id} ({self.name})"


class CustomerGroup(Base):
    id = Column(Integer, primary_key=True)
    internal_id = Column(String(32), unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    customers = relationship(Customer, backref="customer_group", order_by="-Customer.id")

    def __str__(self) -> str:
        return f"{self.internal_id} ({self.name})"
