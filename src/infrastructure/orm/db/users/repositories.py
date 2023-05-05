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
        users = CustomUser.objects.values()
        filtered_users = list(map(lambda x: {'id': x['id'], 'email': x['email'], 'first_name': x['first_name']}, users))
        print('Filtered users:', filtered_users)  # Agrega este registro para verificar los usuarios filtrados
        entities = list(map(lambda x: UserEntity(**x), filtered_users))
        print('User entities:', entities)  # Agrega este registro para verificar las entidades de usuario creadas
        return entities
