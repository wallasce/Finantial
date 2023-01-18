import datetime

class Spent:
    def __init__(self, description: str, value: float, date: datetime, type: str, form: str) -> None:
        self.description = description
        self.value = value
        self.date = date
        self.type = type
        self.form = form
        pass