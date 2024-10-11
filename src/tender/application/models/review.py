from uuid import UUID

from tender.application import Maybe


class Review:
    def __init__(
        self, *, id: UUID, bid_id: UUID, description: str, rating: int
    ) -> None:
        self.id = id
        self.bid_id = bid_id
        self.description = description
        self.rating = rating

    @classmethod
    def create(
        cls, *, id: UUID, bid_id: UUID, description: str, rating: int
    ) -> "Review":
        return Review(
            id=id, bid_id=bid_id, description=description, rating=rating
        )

    def update(
        self,
        *,
        bid_id: Maybe[UUID],
        description: Maybe[str],
        rating: Maybe[str],
    ) -> None:
        if bid_id.is_set:
            self.bid_id = bid_id
        if description.is_set:
            self.description = description
        if rating.is_set:
            self.rating = rating
