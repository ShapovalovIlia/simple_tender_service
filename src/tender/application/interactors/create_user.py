from uuid_extensions import uuid7

from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import UserGateway
from tender.application.commands import CreateUserCommand
from tender.application.models import User


class CreateUserProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        user_gateway: UserGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.user_gateway = user_gateway

    async def process(self, command: CreateUserCommand) -> None:
        user = User.create(
            id=uuid7(),
            first_name=command.first_name,
            last_name=command.last_name,
            username=command.username,
        )
        await self.user_gateway.save(user)
        await self.transaction_manager.commit()
