from uuid_extensions import uuid7

from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import OrganizationGateway
from tender.application.commands import CreateOrganizationCommand
from tender.application.models import Organization


class CreateOrganizationProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        organization_gateway: OrganizationGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.organization_gateway = organization_gateway

    async def process(self, command: CreateOrganizationCommand) -> None:
        organization = Organization.create(
            id=uuid7(),
            name=command.name,
            description=command.description,
            organization_type=command.organization_type,
        )
        await self.organization_gateway.save(organization)
        await self.transaction_manager.commit()
