# coding: utf-8
from typing import List
from src.domain.entities.users import UserEntity
from src.infrastructure.orm.db.users.models import CustomUser
from src.interfaces.repositories.exceptions import EntityDoesNotExist


class UserDatabaseRepository:

    def get(self, code: str) -> UserEntity:
        user = CustomUser.objects.filter(id=id).values().first()
        if not user:
            raise EntityDoesNotExist(f'{code} currency code does not exist')
        return UserEntity(**user)

    def list(self) -> List[UserEntity]:
        users = CustomUser.objects.values()
        filtered_users = list(map(lambda x: {'email': x['email'], 'first_name': x['first_name']}, users))
        entities = list(map(lambda x: UserEntity(**x), filtered_users))
        return entities
