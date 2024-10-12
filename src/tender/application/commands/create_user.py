from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CreateUserCommand:
    first_name: str
    last_name: str
    username: str
