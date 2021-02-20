from enum import Enum
from typing import Tuple

SEX_OPTIONS: Tuple[str, str, str] = ("male", "female", "unknown")
FLOWCELL_STATUS: Tuple[str, str, str, str] = ("ondisk", "removed", "requested", "processing")
CASE_ACTIONS: Tuple[str, str, str] = ("analyze", "running", "hold")
STATUS_OPTIONS: Tuple[str, str, str] = ("affected", "unaffected", "unknown")


class Pipeline(str, Enum):
    BALSAMIC: str = "balsamic"
    FASTQ: str = "fastq"
    FLUFFY: str = "fluffy"
    MICROSALT: str = "microsalt"
    MIP_DNA: str = "mip-dna"
    MIP_RNA: str = "mip-rna"


class DataDelivery(str, Enum):
    FASTQ: str = "fastq"
    QC: str = "custom"
