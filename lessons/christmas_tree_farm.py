from __future__ import annotations

class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        for x in range(0, initial_planting):
            self.plots.append(1)
        for x in range(initial_planting, plots):
            self.plots.append(0)
    
    def plant(self, plot_idx: int):
        self.plots[plot_idx] = 1

    def growth(self):
        for x in range(0, len(self.plots)):
            if self.plots[x] != 1:
                self.plots[x] += 1
    
    def harvest(self, replant: bool) -> int:
        total_trees: int = 0
        for x in range(0, len(self.plots)):
            if self.plots[x] >= 5:
                total_trees += 1
                if replant:
                    self.plots[x] = 1
                else:
                    self.plots[x] = 0

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        trees: int = 0
        for x in self.plots:
            if x >= 1:
                trees += 1
        for a in rhs.plots:
            if a >= 1:
                trees += 1
        return ChristmasTreeFarm(len(self.plots) +len(rhs.plots), trees)