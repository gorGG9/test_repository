class Query:
    """Определяет параметры поиска: поле и значение."""
    def __init__(self, field: str, value: str):
        self._field = field
        self._value = value

    @property
    def field(self) -> str:
        return self._field

    @property
    def value(self) -> str:
        return self._value
