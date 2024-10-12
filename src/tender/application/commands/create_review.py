from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True, frozen=True)
class CreateReviewCommand:
    bid_id: UUID
    description: str
    rating: int
