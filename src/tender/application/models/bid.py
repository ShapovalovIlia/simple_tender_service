from uuid import UUID
from datetime import date

from tender.application.constants import BidStatus
from tender.application.maybe import Maybe


class Bid:
    def __init__(
        self,
        *,
        id: UUID,
        tender_id: UUID,
        creator_id: UUID,
        status: BidStatus,
        name: str,
        description: str,
        price: int,
        start_at: date | None,
        end_at: date | None,
    ) -> None:
        self.id = id
        self.tender_id = tender_id
        self.status = status
        self.creator_id = creator_id
        self.name = name
        self.description = description
        self.price = price
        self.start_at = start_at
        self.end_at = end_at

    @classmethod
    def create(
        cls,
        *,
        id: UUID,
        tender_id: UUID,
        creator_id: UUID,
        name: str,
        description: str,
        price: int,
        start_at: date | None,
        end_at: date | None,
    ) -> "Bid":
        return Bid(
            id=id,
            tender_id=tender_id,
            creator_id=creator_id,
            status=BidStatus.CREATED,
            name=name,
            description=description,
            price=price,
            start_at=start_at,
            end_at=end_at,
        )

    def update(
        self,
        *,
        name: Maybe[str],
        description: Maybe[str],
        price: Maybe[int],
        start_at: Maybe[date | None],
        end_at: Maybe[date | None],
    ) -> None:
        if name.is_set:
            self.name = name.value

        if description.is_set:
            self.description = description.value

        if price.is_set:
            self.price = price.value

        if start_at.is_set:
            self.start_at = start_at.value

        if end_at.is_set:
            self.end_at = end_at.value

    def aprove(self) -> None:
        self.status = BidStatus.IN_PROGRESS

    def cancel(self) -> None:
        self.status = BidStatus.CANCELED

    def close(self) -> None:
        self.status = BidStatus.CLOSED
