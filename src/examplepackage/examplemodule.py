class PhoneBook:
    """A phonebook."""
    def __init__():
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def clear(self):
        self.numbers.clear()
