from error_handler import input_error
from address_book import AddressBook
from record import Record


@input_error
def add_record(args: list, book: AddressBook) -> str:
    name, phone, birthday = None, None, None

    match args:
        case [_name, _phone]:
            name = _name
            phone = _phone
        case [_name, _phone, _birthday]:
            name = _name
            phone = _phone
            birthday = _birthday
        case _:
            raise IndexError

    record = book.find(name)
    if record is not None:
        record.add_phone(phone)
        return "Contact changed"

    new_record = Record(name)
    new_record.add_phone(phone)
    if birthday is not None:
        new_record.add_birthday(birthday)
    book.add_record(new_record)

    return "Contact added"


@input_error
def add_phone(args: list[str], book: AddressBook) -> str:
    name, phone = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_phone(phone)
    return "Contact changed"


@input_error
def change_phone(args: list[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)
    return "Contact changed"


@input_error
def show_phone(args: list, book: AddressBook) -> str:
    (name,) = args
    record = book.find(name)

    if record is None:
        raise KeyError

    return f"{'; '.join(phone.value for phone in record.phones)} "


@input_error
def show_all(book: AddressBook):
    if not book.values():
        print("The address-book is empty")

    for record in book.values():
        print(record)


@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(birthday)
    return "Contact changed"


@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    (name,) = args
    record = book.find(name)

    if record is None:
        raise KeyError

    return f"Birthday of {record.name} is {record.birthday}"


@input_error
def birthdays(book: AddressBook):
    if not book.values():
        print("The address-book is empty")

    upcoming_birthdays = book.get_upcoming_birthdays()

    for name, date in upcoming_birthdays.items():
        print(f"{name}: {date}")


@input_error
def delete(args: list, book: AddressBook):
    (name,) = args
    record = book.find(name)

    if record is None:
        raise KeyError

    book.delete(name)
    return "Contact deleted"
