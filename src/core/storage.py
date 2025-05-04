from core.query import Query
from models.record import Record
from collections import defaultdict

class DataStorage:
    """Хранилище данных с поддержкой индексации и поиска."""
    def __init__(self):
        self._storage = {}
        self._indices = defaultdict(dict)  # Индексы по полям

    def add_record(self, record: Record) -> None:
        self._storage[record.key] = record
        for field, value in record._data.items():
            self._indices[field].setdefault(value, set()).add(record.key)

    def delete_record(self, key: str) -> None:
        if key not in self._storage:
            raise KeyError(f"Record with key {key} not found")
        record = self._storage[key]
        for field, value in record._data.items():
            self._indices[field][value].discard(key)
        del self._storage[key]

    def search(self, query: Query) -> list:
        matched_keys = self._indices.get(query.field, {}).get(query.value, set())
        return [self._storage[k] for k in matched_keys]
