from address_book import AddressBook
from commands import (
    add_record,
    change_phone,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    delete,
)


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command_list = parse_input(user_input)
        match command_list:
            case ["close"] | ["exit"]:
                print("Good bye!")
                break
            case ["hello"]:
                print("Hello!")
            case ["add", *args]:
                print(add_record(args, book))
            case ["change", *args]:
                print(change_phone(args, book))
            case ["phone", *args]:
                print(show_phone(args, book))
            case ["all"]:
                show_all(book)
            case ["add-birthday", *args]:
                print(add_birthday(args, book))
            case ["show-birthday", *args]:
                print(show_birthday(args, book))
            case ["birthdays"]:
                birthdays(book)
            case ["delete", *args]:
                print(delete(args, book))
            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
