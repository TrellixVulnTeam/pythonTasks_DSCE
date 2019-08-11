class AlternativeIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, index):
        return self.data[index]