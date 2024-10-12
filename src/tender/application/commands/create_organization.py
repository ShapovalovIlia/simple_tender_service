from dataclasses import dataclass

from tender.application.constants import OrganizationType


@dataclass(frozen=True, slots=True)
class CreateOrganizationCommand:
    name: str
    description: str
    organization_type: OrganizationType
