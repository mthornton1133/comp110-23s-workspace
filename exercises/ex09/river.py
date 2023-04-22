"""File to define River class."""

__author__ = "730546472"
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """This is the River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the bears and fish and removes ones that are too old."""
        alive_fish: list[Fish] = []
        alive_bears: list[Bear] = []
        i: int = 0
        while i < len(self.fish):
            if self.fish[i].age <= 3:
                alive_fish.append(self.fish[i])
            i += 1
        self.fish = alive_fish
        for idx in range(0, len(self.bears)):
            if self.bears[idx].age <= 5:
                alive_bears.append(self.bears[idx])
        self.bears = alive_bears
        return None

    def bears_eating(self):
        """Simulates the bears eating."""
        for x in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                x.eat(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger of the bears and alters it as needed."""
        surviving_bears: list[Bear] = []
        for i in range(0, len(self.bears)):
            if self.bears[i].hunger_score >= 0:
                surviving_bears.append(self.bears[i])
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Repoulates fish, for every two four are born."""
        num_of_new_fish: int = (len(self.fish) // 2) * 4
        for x in range(0, num_of_new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repoulates bears, for every two one is born."""
        num_of_new_bears: int = len(self.bears) // 2 
        for x in range(0, num_of_new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Use to view current state of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes x amount of fish from the river."""
        for idx in range(0, amount):
            self.fish.pop(idx)
        return None