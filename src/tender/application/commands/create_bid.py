from dataclasses import dataclass
from uuid import UUID
from datetime import date


@dataclass(slots=True, frozen=True)
class CreateBidCommand:
    tender_id: UUID
    creator_id: UUID
    name: str
    description: str
    price: int
    start_at: date | None
    end_at: date | None
