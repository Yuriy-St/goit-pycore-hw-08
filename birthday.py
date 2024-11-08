from datetime import datetime

from constants import DATE_FORMAT
from field import Field


class Birthday(Field):
    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, DATE_FORMAT)
            super().__init__(date)
        except ValueError:
            raise ValueError(f"Date '{value}': Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime(DATE_FORMAT)


if __name__ == "__main__":
    for date in ["20.12.2023", "20.12.23", "20.13.2023", "2024.12.01"]:
        try:
            birthday = Birthday(date)
            print(birthday)
        except Exception as e:
            print(e)
