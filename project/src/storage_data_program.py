class Record:
    def __init__(self, key, data):
        self._key = key
        self._data = data
    
    def get_key(self):
        return self._key
    
    def __getitem__(self, field):
        return self._data.get(field)

class User:
    def __init__(self, user_id: str, name: str):
        self._id = user_id
        self._name = name

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def search(self, query: 'Query', data_storage: 'DataStorage') -> list:
        return data_storage.search(query)

    def add_record(self, record: Record, data_storage: 'DataStorage') -> None:
        data_storage.add_record(record)

    def delete_record(self, key: str, data_storage: 'DataStorage') -> None:
        data_storage.delete_record(key)

class Query:
    def __init__(self, field: str, value: str):
        self.field = field
        self.value = value

    def get_field(self) -> str:
        return self.field

    def get_value(self) -> str:
        return self.value

class DataStorage:
    def __init__(self):
        self._storage = {}
        self._indices = []

    def search(self, query: Query) -> list:
        results = []
        for key, record in self._storage.items():
            if record[query.get_field()] == query.get_value():
                results.append(record)
        return results

    def add_record(self, record: Record) -> None:
        self._storage[record.get_key()] = record

    def delete_record(self, key: str) -> None:
        if key not in self._storage:
            raise KeyError(f"Record with key {key} not found")
        del self._storage[key]
