from dataclasses import dataclass
from uuid import UUID

from tender.application.maybe import Maybe


@dataclass(slots=True, frozen=True)
class UpdateUserCommand:
    id: UUID
    first_name: Maybe[str]
    last_name: Maybe[str]
    username: Maybe[str]
