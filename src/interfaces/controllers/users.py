# coding: utf-8

import logging
from http import HTTPStatus
from typing import Tuple

from src.domain.usecases.users import UserUseCase
from src.interfaces.serializers.users import UserSerializer

logger = logging.getLogger(__name__)


class UserController:

    def __init__(self, users_usecase: UserUseCase):
        self.users_usecase = users_usecase

    def list(self) -> Tuple[list, int]:
        users = self.users_usecase.list()
        return (
            UserSerializer(many=True).dump(users),
            HTTPStatus.OK.value
        )
