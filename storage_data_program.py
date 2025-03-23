class User:
    def __init__(self, user_id: str, name: str):
        self._id = user_id  # Инкапсуляция: защищённый атрибут
        self._name = name  # Инкапсуляция: защищённый атрибут

    def get_id(self) -> str:
        return self._id  # Метод доступа к защищённому атрибуту

    def get_name(self) -> str:
        return self._name  # Метод доступа к защищённому атрибуту

    def search(self, query: 'Query', data_storage: 'DataStorage') -> list:
        # Использование ассоциации: User взаимодействует с DataStorage
        return data_storage.search(query)

    def add_record(self, record: 'Record', data_storage: 'DataStorage') -> None:
        # Использование ассоциации: User взаимодействует с DataStorage
        data_storage.add_record(record)

    def delete_record(self, key: str, data_storage: 'DataStorage') -> None:
        # Использование ассоциации: User взаимодействует с DataStorage
        data_storage.delete_record(key)

class Query:
    def __init__(self, field: str, value: str):
        self.field = field  # Публичный атрибут
        self.value = value  # Публичный атрибут

    def get_field(self) -> str:
        return self.field  # Метод доступа

    def get_value(self) -> str:
        return self.value  # Метод доступа

class DataStorage:
    def __init__(self):
        self._storage = {}  # Инкапсуляция: защищённый атрибут
        self._indices = []  # Инкапсуляция: защищённый атрибут

    def search(self, query: Query) -> list:
        # Использование ассоциации: DataStorage взаимодействует с Query
        results = []
        for key, record in self._storage.items():
            if query.get_field() in record and record[query.get_field()] == query.get_value():
                results.append(record)
        return results

    def add_record(self, record: 'Record') -> None:
        # Добавление записи в хранилище
        self._storage[record.get_key()] = record

    def delete_record(self, key: str) -> None:
        # Удаление записи из хранилища
        if key in self._storage:
            del self._storage[key]
