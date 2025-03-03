class DatabaseConnection:
    # Статическая переменная для хранения единственного экземпляра
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Если экземпляр еще не создан, создаем его
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Инициализируем подключение к базе данных
            cls._instance.connection = "Database Connection Established"
        # Возвращаем единственный экземпляр
        return cls._instance

    # Метод для получения подключения
    def get_connection(self):
        return self.connection

# Проверка работы Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()

# Оба объекта db1 и db2 ссылаются на один и тот же экземпляр
print(db1.get_connection())  # Вывод: Database Connection Established
print(db2.get_connection())  # Вывод: Database Connection Established
print(db1 is db2)            # Вывод: True (это один и тот же объект)
