from dataclasses import dataclass
from datetime import date
from uuid import UUID

from tender.application.constants.job_type import JobType
from tender.application.maybe import Maybe


@dataclass(slots=True, frozen=True)
class UpdateTenderCommand:
    id: UUID
    job_type: Maybe[JobType]
    name: Maybe[str]
    description: Maybe[str]
    min_price: Maybe[int]
    max_price: Maybe[int]
    start_at: Maybe[date | None]
    end_at: Maybe[date | None]
