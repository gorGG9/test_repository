class Record:
    """Представляет собой запись в хранилище данных."""
    def __init__(self, key: str, data: dict):
        self._key = key
        self._data = data

    @property
    def key(self) -> str:
        return self._key

    def get_field(self, field: str):
        return self._data.get(field)
