from datetime import datetime

from dolores.constants import FLOWCELL_STATUS
from dolores.db.base_class import Base
from dolores.models.sample import flowcell_sample
from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import relationship


class Flowcell(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    sequencer_type = Column(Enum("hiseqga", "hiseqx", "novaseq"))
    sequencer_name = Column(String(32))
    sequenced_at = Column(DateTime)
    status = Column(Enum(*FLOWCELL_STATUS), default="ondisk")
    archived_at = Column(DateTime)
    updated_at = Column(DateTime, onupdate=datetime.now)

    samples = relationship("Sample", secondary=flowcell_sample, backref="flowcells")

    def __str__(self):
        return self.name

    def to_dict(self, samples: bool = False):
        """Represent as dictionary"""
        data = super(Flowcell, self).to_dict()
        if samples:
            data["samples"] = [sample.to_dict() for sample in self.samples]
        return data
