from typing import Protocol
from uuid import UUID

from tender.application.models import Bid


class BidGateway(Protocol):
    async def save(self, bid: Bid) -> None:
        raise NotImplementedError

    async def by_id(self, id: UUID) -> Bid | None:
        raise NotImplementedError

    async def update(self, bid: Bid) -> None:
        raise NotImplementedError
