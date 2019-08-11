class Phonebook:

    def __init__(self):
        self.entries = {}
        self.is_right = True

    def add(self, name, number):
        for numbers in self.entries.values():
            if number in numbers or number == numbers:
                self.is_right = False
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def names(self):
        return self.entries.keys()

    def numbers(self):
        return self.entries.values()

    def is_consistent(self):
        return self.is_right
