# coding: utf-8
from src.domain.usecases.users import UserUseCase
from src.infrastructure.orm.cache.users import UserCacheRepository
from src.infrastructure.orm.db.users.repositories import UserDatabaseRepository
from src.interfaces.controllers.users import UserController
from src.interfaces.repositories.users import UserRepository


class UserDatabaseRepositoryFactory:

    @staticmethod
    def get() -> UserDatabaseRepository:
        return UserDatabaseRepository()


class UserCacheRepositoryFactory:

    @staticmethod
    def get() -> UserCacheRepository:
        return UserCacheRepository()


class UserRepositoryFactory:

    @staticmethod
    def get() -> UserRepository:
        db_repo = UserDatabaseRepositoryFactory.get()
        cache_repo = UserCacheRepositoryFactory.get()
        return UserRepository(db_repo, cache_repo)


class UserUseCaseFactory:

    @staticmethod
    def get() -> UserUseCase:
        user_repo = UserRepositoryFactory.get()
        return UserUseCase(user_repo)


class UserViewSetFactory:

    @staticmethod
    def create() -> UserController:
        user_usecase = UserUseCaseFactory.get()
        return UserController(
            user_usecase,
        )
