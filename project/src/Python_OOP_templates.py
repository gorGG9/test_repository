# Базовый класс для управления хранилищем данных
class DataStorage:
    def __init__(self):
        # Приватная переменная для хранения данных (инкапсуляция)
        self._data = []
        self._index = {}

    # Публичный метод для добавления данных
    def add_data(self, item):
        self._data.append(item)
        self._update_index(item)  # Приватный метод для обновления индекса

    # Публичный метод для поиска данных
    def search_data(self, query):
        raise NotImplementedError("Этот метод должен быть переопределен в дочерних классах")

    # Приватный метод для обновления индекса (инкапсуляция)
    def _update_index(self, item):
        # Пример простой индексации
        if isinstance(item, str):
            self._index[item] = len(self._data) - 1

    # Публичный метод для получения данных (инкапсуляция)
    def get_data(self):
        return self._data


# Класс для индексированного хранилища (наследование)
class IndexedStorage(DataStorage):
    def __init__(self):
        super().__init__()
        self._index_type = "hash"  # Пример типа индекса

    # Переопределение метода поиска (полиморфизм)
    def search_data(self, query):
        if query in self._index:
            return self._data[self._index[query]]
        return None


# Класс для быстрого поиска (наследование)
class FastSearchStorage(DataStorage):
    def __init__(self):
        super().__init__()

    # Переопределение метода поиска (полиморфизм)
    def search_data(self, query):
        # Пример быстрого поиска через бинарный поиск (предполагаем, что данные отсортированы)
        low, high = 0, len(self._data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self._data[mid] == query:
                return self._data[mid]
            elif self._data[mid] < query:
                low = mid + 1
            else:
                high = mid - 1
        return None


# Пример использования
if __name__ == "__main__":
    # Использование IndexedStorage
    indexed_storage = IndexedStorage()
    indexed_storage.add_data("apple")
    indexed_storage.add_data("banana")
    print(indexed_storage.search_data("banana"))

    # Использование FastSearchStorage
    fast_storage = FastSearchStorage()
    fast_storage.add_data("apple")
    fast_storage.add_data("banana")
    print(fast_storage.search_data("apple"))
