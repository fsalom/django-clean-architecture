# coding: utf-8
import dataclasses
import json
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
        return list(map(lambda x: UserEntity(**x), CustomUser.objects.values()))
