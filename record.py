from name import Name
from phone import Phone
from birthday import Birthday


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def add_birthday(self, value: str):
        self.birthday = Birthday(value)

    def find_phone(self, value: str) -> Phone | None:
        result = [item for item in self.phones if item.value == value]
        return result[0] if result else None

    def add_phone(self, value: str):
        phone = self.find_phone(value)
        if phone is not None:
            raise Exception(f"Phone number '{value}' already exists in the record")
        self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        self.phones = [phone for phone in self.phones if phone.value != value]

    def edit_phone(self, old_value: str, new_value: str):
        phone = self.find_phone(old_value)
        if phone is None:
            raise ValueError(f"Phone number '{old_value}' not found")

        # Don't remove the old value before adding the new one - it could be invalid
        self.add_phone(new_value)
        self.remove_phone(old_value)

    def __str__(self):
        birthday_str = f"; birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"


if __name__ == "__main__":
    try:
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")
        # john_record.remove_phone("5555555555")
        # john_record.edit_phone("5555555555", "werw")
        john_record.edit_phone("5555555555", "1234567880")
    except Exception as e:
        print(e)
    finally:
        print(john_record)
