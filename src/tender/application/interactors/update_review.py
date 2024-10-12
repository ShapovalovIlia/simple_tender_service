from tender.application.transaction_manager import TransactionManager
from tender.application.gateways import ReviewGateway
from tender.application.commands import UpdateReviewCommand


class UpdateReviewProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        review_gateway: ReviewGateway,
    ) -> None:
        self.transaction_manager = transaction_manager
        self.review_gateway = review_gateway

    async def process(self, command: UpdateReviewCommand) -> None:
        review = await self.review_gateway.by_id(command.id)
        if not review:
            raise Exception()  # TODO

        review.update(description=command.description, rating=command.rating)
        await self.review_gateway.update(review)
        await self.transaction_manager.commit()
