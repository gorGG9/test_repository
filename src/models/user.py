from core.query import Query
from core.storage import DataStorage
from models.record import Record

class User:
    """Представляет пользователя системы."""
    def __init__(self, user_id: str, name: str):
        self._id = user_id
        self._name = name

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def search_records(self, query: Query, storage: DataStorage) -> list:
        return storage.search(query)

    def add_record(self, record: Record, storage: DataStorage) -> None:
        storage.add_record(record)

    def delete_record(self, key: str, storage: DataStorage) -> None:
        storage.delete_record(key)
