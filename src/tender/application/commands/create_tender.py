from dataclasses import dataclass
from datetime import date

from tender.application.constants.job_type import JobType


@dataclass(slots=True, frozen=True)
class CreateTenderCommand:
    job_type: JobType
    name: str
    description: str
    min_price: int
    max_price: int
    start_at: date | None
    end_at: date | None
