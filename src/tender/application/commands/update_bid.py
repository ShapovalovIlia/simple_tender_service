from dataclasses import dataclass
from datetime import date
from uuid import UUID

from tender.application.maybe import Maybe


@dataclass(slots=True, frozen=True)
class UpdateBidCommand:
    id: UUID
    name: Maybe[str]
    description: Maybe[str]
    price: Maybe[int]
    start_at: Maybe[date | None]
    end_at: Maybe[date | None]
