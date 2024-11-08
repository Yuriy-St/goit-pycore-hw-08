from typing import Callable


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the all arguments"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Enter correct arguments"
        except Exception as e:
            return str(e)

    return inner
