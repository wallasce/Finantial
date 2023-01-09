import datetime

class Spent:
    def __init__(self, name: str, value: float, date: datetime, type: str, form: str) -> None:
        self.name = name
        self.value = value
        self.date = date
        self.type = type
        self.form = form
        pass