from enum import Enum


class BidStatus(Enum):
    CREATED = "Created"
    CANCELED = "Canceled"
    IN_PROGRESS = "In progress"
    CLOSED = "Closed"
