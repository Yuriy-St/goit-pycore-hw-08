class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __eq__(self, other: "Field") -> bool:
        return self.value == other.value

    def __str__(self):
        return str(self.value)
