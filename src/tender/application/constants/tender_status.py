from enum import Enum


class TenderStatus(Enum):
    CREATED = "Created"
    PUBLISHED = "Published"
    HIDDEN = "Hidden"
    CLOSED = "Closed"
    CANCELED = "Canceled"
