from typing import Protocol
from uuid import UUID

from tender.application.models import User


class UserGateway(Protocol):
    async def save(self, user: User) -> None:
        raise NotImplementedError

    async def by_id(self, id: UUID) -> User | None:
        raise NotImplementedError

    async def update(self, user: User) -> None:
        raise NotImplementedError
