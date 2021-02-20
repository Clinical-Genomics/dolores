# -*- coding: utf-8 -*-
import datetime as dt
from typing import List

import alchy
from cg.constants import (
    CASE_ACTIONS,
    FLOWCELL_STATUS,
    PREP_CATEGORIES,
    PRIORITY_MAP,
    REV_PRIORITY_MAP,
    SEX_OPTIONS,
    STATUS_OPTIONS,
    DataDelivery,
    Pipeline,
)
from sqlalchemy import Column, ForeignKey, Table, UniqueConstraint, orm, types

Model = alchy.make_declarative_base(Base=alchy.ModelBase)


flowcell_sample = Table(
    "flowcell_sample",
    Model.metadata,
    Column("flowcell_id", types.Integer, ForeignKey("flowcell.id"), nullable=False),
    Column("sample_id", types.Integer, ForeignKey("sample.id"), nullable=False),
    UniqueConstraint("flowcell_id", "sample_id", name="_flowcell_sample_uc"),
)
