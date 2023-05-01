from typing import List

from src.domain.entities.users import UserEntity


class UserUseCase:

    def __init__(self, users_repo: object):
        self.users_repo = users_repo

    def list(self) -> List[UserEntity]:
        return self.users_repo.list()
