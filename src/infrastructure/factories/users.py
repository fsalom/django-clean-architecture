# coding: utf-8

from src.infrastructure.factories.provider import ProviderClientInteractorFactory
from src.infrastructure.orm.cache.exchange_rate.repositories import (
    CurrencyCacheRepository, CurrencyExchangeRateCacheRepository)
from src.infrastructure.orm.db.exchange_rate.repositories import (
    CurrencyDatabaseRepository, CurrencyExchangeRateDatabaseRepository)
from src.interface.controllers.exchange_rate import (
    CurrencyController, CurrencyExchangeRateController)
from src.interface.repositories.exchange_rate import (
    CurrencyRepository, CurrencyExchangeRateRepository)
from src.usecases.exchange_rate import (
    CurrencyInteractor, CurrencyExchangeRateInteractor)

from src.domain.usecases.users import UserUseCase
from src.infrastructure.orm.db.users.repositories import UserDatabaseRepository
from src.interfaces.controllers.users import UserController


class UserDatabaseRepositoryFactory:

    @staticmethod
    def get() -> UserDatabaseRepository:
        return UserDatabaseRepository()


class UserCacheRepositoryFactory:

    @staticmethod
    def get() -> CurrencyCacheRepository:
        return CurrencyCacheRepository()


class UserRepositoryFactory:

    @staticmethod
    def get() -> CurrencyRepository:
        db_repo = UserDatabaseRepositoryFactory.get()
        cache_repo = UserCacheRepositoryFactory.get()
        return CurrencyRepository(db_repo, cache_repo)


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
