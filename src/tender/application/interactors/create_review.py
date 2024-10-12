from uuid_extensions import uuid7

from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import ReviewGateway
from tender.application.commands import CreateReviewCommand
from tender.application.models import Review


class CreateReviewProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        review_gateway: ReviewGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.review_gateway = review_gateway

    async def process(self, command: CreateReviewCommand) -> None:
        review = Review.create(
            id=uuid7(),
            bid_id=command.bid_id,
            description=command.description,
            rating=command.rating,
        )
        await self.review_gateway.save(review)
        await self.transaction_manager.commit()
