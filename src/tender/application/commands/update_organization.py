from dataclasses import dataclass
from uuid import UUID

from tender.application.maybe import Maybe
from tender.application.constants import OrganizationType


@dataclass(frozen=True, slots=True)
class UpdateOrganizationCommand:
    id: UUID
    name: Maybe[str]
    description: Maybe[str]
    organization_type: Maybe[OrganizationType]
