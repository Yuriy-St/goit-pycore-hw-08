from datetime import datetime, timedelta

from collections import UserDict

from record import Record
from constants import FRIDAY, WEEK, DATE_FORMAT


class AddressBook(UserDict[str, Record]):

    def find(self, name: str) -> Record | None:
        result = [record for record in self.data if record == name]
        if result:
            record_name = result[0]
            return self.data[record_name]
        else:
            return None

    def add_record(self, record: Record):
        if self.find(record.name.value) is not None:
            raise KeyError(
                f"Record with name '{record.name.value}' already exists in the addressbook"
            )

        self.data[record.name.value] = record

    def get_upcoming_birthdays(self):
        congratulation_dates: dict[str, str] = {}
        today = datetime.today().date()
        for record in self.data.values():
            birthday = record.birthday
            if birthday is None:
                break
            congratulation_date = birthday.value.replace(year=today.year).date()
            dif = (congratulation_date - today).days

            if 0 <= dif < WEEK:
                weekday = congratulation_date.isoweekday()
                # check if this year birthday is at the weekend
                if FRIDAY < weekday:
                    days_to_monday = timedelta(days=(WEEK - weekday + 1))
                    congratulation_date += days_to_monday

                congratulation_dates[record.name.value] = congratulation_date.strftime(
                    DATE_FORMAT
                )

        return congratulation_dates

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    try:
        # Створення нової адресної книги
        book = AddressBook()

        # Створення запису для John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")

        # Додавання запису John до адресної книги
        book.add_record(john_record)
    except Exception as e:
        print(e)
