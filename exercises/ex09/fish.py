"""File to define Fish class."""


class Fish:
    """This is the Fish class."""
    age: int

    def __init__(self):
        """Method to construct class."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one day in fishes life."""
        self.age += 1
        return None