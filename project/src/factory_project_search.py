class FullTextSearch:
    def search(self, query):
        # Возвращает результаты полнотекстового поиска
        return f"Full-text search results for '{query}'"

class IndexSearch:
    def search(self, query):
        # Возвращает результаты поиска по индексу
        return f"Index search results for '{query}'"

class SearchFactory:
    @staticmethod
    def create_search(type):
        # В зависимости от типа создаем соответствующий объект поиска
        if type == "fulltext":
            return FullTextSearch()
        elif type == "index":
            return IndexSearch()
        else:
            # Если тип неизвестен, выбрасываем исключение
            raise ValueError("Unknown search type")

# Проверка работы Factory
factory = SearchFactory()

# Создаем объект для полнотекстового поиска
search1 = factory.create_search("fulltext")
# Создаем объект для поиска по индексу
search2 = factory.create_search("index")

# Используем созданные объекты для поиска
print(search1.search("data"))  # Вывод: Full-text search results for 'data'
print(search2.search("data"))  # Вывод: Index search results for 'data'
