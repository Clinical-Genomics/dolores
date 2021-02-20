from dolores.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)

    customer_id = Column(
        Integer, ForeignKey("customer.id", ondelete="CASCADE", use_alter=True), nullable=False
    )
    customer = relationship("Customer", foreign_keys=[customer_id])

    def __str__(self) -> str:
        return self.name
