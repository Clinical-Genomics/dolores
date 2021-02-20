class Analysis(Model):
    id = Column(types.Integer, primary_key=True)
    pipeline = Column(types.Enum(*list(Pipeline)))
    pipeline_version = Column(types.String(32))
    started_at = Column(types.DateTime)
    completed_at = Column(types.DateTime)
    delivery_report_created_at = Column(types.DateTime)
    upload_started_at = Column(types.DateTime)
    uploaded_at = Column(types.DateTime)
    cleaned_at = Column(types.DateTime)
    # primary analysis is the one originally delivered to the customer
    is_primary = Column(types.Boolean, default=False)

    created_at = Column(types.DateTime, default=dt.datetime.now, nullable=False)
    family_id = Column(ForeignKey("family.id", ondelete="CASCADE"))

    def __str__(self):
        return f"{self.family.internal_id} | {self.completed_at.date()}"

    def to_dict(self, family: bool = True):
        """Represent as dictionary"""
        data = super(Analysis, self).to_dict()
        if family:
            data["family"] = self.family.to_dict()
        return data
