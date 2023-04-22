"""File to define Bear class."""


class Bear:
    """This is the Bear class with two attributes."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Method to construct the class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulates one day in bears life."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Bears hunger score increases by the number of fish."""
        self.hunger_score += num_fish
        return None