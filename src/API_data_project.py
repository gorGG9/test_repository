from elasticsearch import Elasticsearch
import requests

class ElasticsearchAdapter(ExternalServiceAdapter):
    def __init__(self, host: str, port: int):
        self.client = Elasticsearch([{'host': host, 'port': port}])

    def connect(self, **kwargs):
        if not self.client.ping():
            raise ConnectionError("Не удалось подключиться к Elasticsearch")

    def search(self, query: str, **kwargs):
        index = kwargs.get('index', 'default_index')
        body = {
            "query": {
                "match": {
                    "content": query
                }
            }
        }
        return self.client.search(index=index, body=body)

    def index_data(self, data: dict, **kwargs):
        index = kwargs.get('index', 'default_index')
        return self.client.index(index=index, body=data)

    def close(self):
        self.client.close()

class RestApiAdapter(ExternalServiceAdapter):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def connect(self, **kwargs):
        response = requests.get(f"{self.base_url}/health")
        if response.status_code != 200:
            raise ConnectionError("Не удалось подключиться к REST API")

    def search(self, query: str, **kwargs):
        endpoint = kwargs.get('endpoint', 'search')
        params = {'query': query}
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        return response.json()

    def index_data(self, data: dict, **kwargs):
        endpoint = kwargs.get('endpoint', 'index')
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        return response.json()

    def close(self):
        pass  # REST API не требует закрытия соединения

def main():
    # Использование ElasticsearchAdapter
    es_adapter = ElasticsearchAdapter(host='localhost', port=9200)
    es_adapter.connect()
    es_adapter.index_data({"content": "Пример данных для индексации"}, index="my_index")
    results = es_adapter.search("Пример")
    print(results)
    es_adapter.close()

    # Использование RestApiAdapter
    rest_adapter = RestApiAdapter(base_url="")
    rest_adapter.connect()
    rest_adapter.index_data({"content": "Пример данных для индексации"}, endpoint="data")
    results = rest_adapter.search("Пример", endpoint="search")
    print(results)
    rest_adapter.close()

if __name__ == "__main__":
    main()
