from enum import Enum


class JobStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class PaidMediaPrior(str, Enum):
    ROI = "ROI"
    MROI = "MROI"
    CUSTOM = "CUSTOM"
