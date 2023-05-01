from dataclasses import dataclass


@dataclass
class UserEntity:
    email: str = None
    first_name: str = None

    @staticmethod
    def to_string(user: 'UserEntity') -> str:
        return f'{user.email} {user.first_name}'
