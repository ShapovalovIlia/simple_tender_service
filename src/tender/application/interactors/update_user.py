from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import UserGateway
from tender.application.commands import UpdateUserCommand


class UpdateUserProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        user_gateway: UserGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.user_gateway = user_gateway

    async def process(self, command: UpdateUserCommand) -> None:
        user = await self.user_gateway.by_id(command.id)
        if not user:
            raise Exception()  # TODO

        user.update(
            first_name=command.first_name,
            last_name=command.last_name,
            username=command.username,
        )
        await self.user_gateway.update(user)
        await self.transaction_manager.commit()
