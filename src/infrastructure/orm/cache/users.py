from typing import List, Union
from django.core.cache import cache
from src.domain.entities.users import UserEntity


CACHE_AVAILABLE_CURRENCIES_KEY = 'cache_available_currencies_key'
CACHE_EXCHANGE_RATE_KEY = '{source_currency}_{exchanged_currency}_{valuation_date}'


class UserCacheRepository:

    def get(self, key: str) -> UserEntity:
        return cache.get(key)

    def list(self) -> List[UserEntity]:
        return self.get(CACHE_AVAILABLE_CURRENCIES_KEY)

    def save(self, key: str, value: Union[UserEntity, list]):
        cache.set(key, value)

    def save_availables(self, currencies: List[UserEntity]):
        self.save(CACHE_AVAILABLE_CURRENCIES_KEY, currencies)
