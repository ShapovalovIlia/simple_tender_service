from dataclasses import dataclass
from uuid import UUID

from tender.application.maybe import Maybe


@dataclass(slots=True, frozen=True)
class UpdateReviewCommand:
    id: UUID
    description: Maybe[str]
    rating: Maybe[int]
