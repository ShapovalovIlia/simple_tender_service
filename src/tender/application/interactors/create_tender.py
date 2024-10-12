from uuid_extensions import uuid7

from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import TenderGateway
from tender.application.commands import CreateTenderCommand
from tender.application.models import Tender


class CreateTenderProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        tender_gateway: TenderGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.tender_gateway = tender_gateway

    async def process(self, command: CreateTenderCommand) -> None:
        tender = Tender.create(
            id=uuid7(),
            job_type=command.job_type,
            name=command.name,
            description=command.description,
            min_price=command.min_price,
            max_price=command.max_price,
            start_at=command.start_at,
            end_at=command.end_at,
        )
        await self.tender_gateway.save(tender)
        await self.transaction_manager.commit()
