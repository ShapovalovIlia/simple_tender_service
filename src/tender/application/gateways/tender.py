from typing import Protocol
from uuid import UUID

from tender.application.models import Tender


class TenderGateway(Protocol):
    async def save(self, tender: Tender) -> None:
        raise NotImplementedError

    async def by_id(self, id: UUID) -> Tender | None:
        raise NotImplementedError

    async def update(self, tender: Tender) -> None:
        raise NotImplementedError
