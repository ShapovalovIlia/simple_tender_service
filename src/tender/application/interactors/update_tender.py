from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import TenderGateway
from tender.application.commands import UpdateTenderCommand


class UpdateTenderProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        tender_gateway: TenderGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.tender_gateway = tender_gateway

    async def process(self, command: UpdateTenderCommand) -> None:
        tender = await self.tender_gateway.by_id(command.id)
        if not tender:
            raise Exception()  # TODO

        tender.update(
            job_type=command.job_type,
            name=command.name,
            description=command.description,
            min_price=command.min_price,
            max_price=command.max_price,
            start_at=command.start_at,
            end_at=command.end_at,
        )
        await self.tender_gateway.update(tender)
        await self.transaction_manager.commit()
