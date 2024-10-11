from uuid import UUID

from tender.application.constants import OrganizationType
from tender.application import Maybe


class Organization:
    def __init__(
        self,
        *,
        id: UUID,
        name: str,
        description: str,
        organization_type: OrganizationType,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.organization_type = organization_type

    @classmethod
    def create(
        cls,
        *,
        id: UUID,
        name: str,
        description: str,
        organization_type: OrganizationType,
    ) -> "Organization":
        return Organization(
            id=id,
            name=name,
            description=description,
            organization_type=organization_type,
        )

    def update(
        self,
        *,
        name: Maybe[str],
        description: Maybe[str],
        organization_type: Maybe[OrganizationType],
    ) -> None:
        if name.is_set:
            self.name = name
        if description.is_set:
            self.description = description
        if organization_type.is_set:
            self.organization_type = organization_type
