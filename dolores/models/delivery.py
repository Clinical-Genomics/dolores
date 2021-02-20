from dolores.db.base_class import Base
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, Text


class Delivery(Base):
    id = Column(Integer, primary_key=True)
    delivered_at = Column(DateTime)
    removed_at = Column(DateTime)
    destination = Column(Enum("caesar", "pdc", "uppmax", "mh", "custom"), default="caesar")
    sample_id = Column(ForeignKey("sample.id", ondelete="CASCADE"))
    pool_id = Column(ForeignKey("pool.id", ondelete="CASCADE"))
    comment = Column(Text)
