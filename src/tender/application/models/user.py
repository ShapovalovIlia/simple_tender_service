from uuid import UUID

from tender.application import Maybe


class User:
    def __init__(
        self,
        *,
        id: UUID,
        first_name: str,
        last_name: str,
        username: str,
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @classmethod
    def create(
        cls, *, id: UUID, first_name: str, last_name: str, username: str
    ) -> "User":
        return User(
            id=id,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

    def update(
        self,
        *,
        first_name: Maybe[str],
        last_name: Maybe[str],
        username: Maybe[str],
    ) -> None:
        if first_name.is_set:
            self.first_name = first_name
        if last_name.is_set:
            self.last_name = last_name
        if username.is_set:
            self.username = username
