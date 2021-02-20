class Bed(Model):
    """Model for bed target captures """

    id = Column(types.Integer, primary_key=True)
    name = Column(types.String(32), unique=True, nullable=False)
    comment = Column(types.Text)
    is_archived = Column(types.Boolean, default=False)
    created_at = Column(types.DateTime, default=dt.datetime.now)
    updated_at = Column(types.DateTime, onupdate=dt.datetime.now)

    versions = orm.relationship("BedVersion", order_by="BedVersion.version", backref="bed")

    def __str__(self) -> str:
        return self.name


class BedVersion(Model):
    """Model for bed target captures versions """

    __table_args__ = (UniqueConstraint("bed_id", "version", name="_app_version_uc"),)

    id = Column(types.Integer, primary_key=True)
    shortname = Column(types.String(64))
    version = Column(types.Integer, nullable=False)
    filename = Column(types.String(256), nullable=False)
    checksum = Column(types.String(32))
    panel_size = Column(types.Integer)
    genome_version = Column(types.String(32))
    designer = Column(types.String(256))
    comment = Column(types.Text)
    created_at = Column(types.DateTime, default=dt.datetime.now)
    updated_at = Column(types.DateTime, onupdate=dt.datetime.now)
    bed_id = Column(ForeignKey(Bed.id), nullable=False)

    def __str__(self) -> str:
        return f"{self.bed.name} ({self.version})"

    def to_dict(self, bed: bool = True):
        """Represent as dictionary"""
        data = super(BedVersion, self).to_dict()
        if bed:
            data["bed"] = self.bed.to_dict()
        return data
