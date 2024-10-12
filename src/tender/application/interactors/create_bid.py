from uuid_extensions import uuid7

from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import BidGateway
from tender.application.commands import CreateBidCommand
from tender.application.models import Bid


class CreateBidProcessor:
    def __init__(
        self, transaction_manager: TransactionManager, bid_gateway: BidGateway
    ) -> None:
        self.transaction_manager = transaction_manager
        self.bid_gateway = bid_gateway

    async def process(self, command: CreateBidCommand) -> None:
        bid = Bid.create(
            id=uuid7(),
            tender_id=command.tender_id,
            creator_id=command.creator_id,
            name=command.name,
            description=command.description,
            price=command.price,
            start_at=command.start_at,
            end_at=command.end_at,
        )
        await self.bid_gateway.save(bid)
        await self.transaction_manager.commit()
