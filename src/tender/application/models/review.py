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
        description: Maybe[str],
        rating: Maybe[int],
    ) -> None:
        if description.is_set:
            self.description = description.value
        if rating.is_set:
            self.rating = rating.value
