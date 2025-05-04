DEFAULT_CONNECTION_STATUS = "Database Connection Established"

class DatabaseConnection:
    # Статическая переменная для хранения единственного экземпляра
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Если экземпляр еще не создан, создаем его
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Инициализируем подключение к базе данных
            cls._instance._connection = DEFAULT_CONNECTION_STATUS
        # Возвращаем единственный экземпляр
        return cls._instance

    # Метод для получения подключения
    @property
    def connection(self) -> str:
        return self._connection

if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(db1.connection())
    print(db2.connection())
    print(db1 is db2)
