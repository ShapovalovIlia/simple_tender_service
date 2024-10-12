from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import OrganizationGateway
from tender.application.commands import UpdateOrganizationCommand


class UpdateOrganizationProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        organization_gateway: OrganizationGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.organization_gateway = organization_gateway

    async def process(self, command: UpdateOrganizationCommand) -> None:
        organization = await self.organization_gateway.by_id(command.id)
        if not organization:
            raise Exception()  # TODO

        organization.update(
            name=command.name,
            description=command.description,
            organization_type=command.organization_type,
        )
        await self.organization_gateway.update(organization)
        await self.transaction_manager.commit()
