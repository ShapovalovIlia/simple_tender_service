from typing import Protocol
from uuid import UUID

from tender.application.models import Review


class ReviewGateway(Protocol):
    async def save(self, review: Review) -> None:
        raise NotImplementedError

    async def by_id(self, id: UUID) -> Review | None:
        raise NotImplementedError

    async def update(self, review: Review) -> None:
        raise NotImplementedError
