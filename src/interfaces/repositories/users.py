from typing import List

from src.domain.entities.users import UserEntity


class UserRepository:

    def __init__(self, db_repo: object, cache_repo: object):
        self.db_repo = db_repo
        self.cache_repo = cache_repo

    def list(self) -> List[UserEntity]:
        users = self.cache_repo.list()
        if not users:
            users = self.db_repo.list()
        return users
