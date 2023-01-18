import datetime

class Gain:
    def __init__(self, description: str, value: float, date: datetime) -> None:
        self.description = description
        self.value = value
        self.date = date
        pass