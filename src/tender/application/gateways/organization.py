from typing import Protocol
from uuid import UUID

from tender.application.models import Organization


class OrganizationGateway(Protocol):
    async def save(self, organization: Organization) -> None:
        raise NotImplementedError

    async def by_id(self, id: UUID) -> Organization | None:
        raise NotImplementedError

    async def update(self, organization: Organization) -> None:
        raise NotImplementedError
