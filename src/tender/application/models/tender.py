from uuid import UUID
from datetime import date

from tender.application.constants import JobType, TenderStatus
from tender.application import Maybe


class Tender:
    def __init__(
        self,
        *,
        id: UUID,
        job_type: JobType,
        tender_status: TenderStatus,
        name: str,
        description: str,
        min_price: int,
        max_price: int,
        start_at: date | None,
        end_at: date | None,
    ) -> None:
        self.id = id
        self.job_type = job_type
        self.tender_status = tender_status
        self.name = name
        self.description = description
        self.min_price = min_price
        self.max_price = max_price
        self.start_at = start_at
        self.end_at = end_at

    @classmethod
    def create(
        cls,
        *,
        id: UUID,
        job_type: JobType,
        name: str,
        description: str,
        min_price: int,
        max_price: int,
        start_at: date | None,
        end_at: date | None,
    ) -> "Tender":
        return Tender(
            id=id,
            job_type=job_type,
            tender_status=TenderStatus.CREATED,
            name=name,
            description=description,
            min_price=min_price,
            max_price=max_price,
            start_at=start_at,
            end_at=end_at,
        )

    def update(
        self,
        *,
        job_type: Maybe[JobType],
        name: Maybe[str],
        description: Maybe[str],
        min_price: Maybe[int],
        max_price: Maybe[int],
        start_at: Maybe[date | None],
        end_at: Maybe[date | None],
    ) -> None:
        if job_type.is_set:
            self.job_type = job_type
        if name.is_set:
            self.name = name
        if description.is_set:
            self.description = description
        if min_price.is_set:
            self.min_price = min_price
        if max_price.is_set:
            self.max_price
        if start_at.is_set:
            self.start_at = start_at
        if end_at.is_set:
            self.end_at = end_at

    def close(self) -> None:
        self.tender_status = TenderStatus.CLOSED

    def hide(self) -> None:
        self.tender_status = TenderStatus.HIDDEN

    def public(self) -> None:
        self.tender_status = TenderStatus.PUBLISHED

    def cancel(self) -> None:
        self.tender_status = TenderStatus.CANCELED
