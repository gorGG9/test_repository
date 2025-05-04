FULLTEXT = "fulltext"
INDEX = "index"

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
    def create_search(search_type: str) -> object:
        # В зависимости от типа создаем соответствующий объект поиска
        if search_type == FULLTEXT:
            return FullTextSearch()
        elif search_type == INDEX:
            return IndexSearch()
        else:
            # Если тип неизвестен, выбрасываем исключение
            raise ValueError("Unknown search type")

if __name__ == "__main__":
    factory = SearchFactory()
    search1 = factory.create_search(FULLTEXT)
    search2 = factory.create_search(INDEX)
    print(search1.search("data"))
    print(search2.search("data"))
