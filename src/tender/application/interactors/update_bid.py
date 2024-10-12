from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import BidGateway
from tender.application.commands import UpdateBidCommand


class UpdateBidProcessor:
    def __init__(
        self, transaction_manager: TransactionManager, bid_gateway: BidGateway
    ) -> None:
        self.transaction_manager = transaction_manager
        self.bid_gateway = bid_gateway

    async def process(self, command: UpdateBidCommand) -> None:
        bid = await self.bid_gateway.by_id(command.id)
        if not bid:
            raise Exception()  # TODO

        bid.update(
            name=command.name,
            description=command.description,
            price=command.price,
            start_at=command.start_at,
            end_at=command.end_at,
        )
        await self.bid_gateway.update(bid)
        await self.transaction_manager.commit()
