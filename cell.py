class Cell:
    def __init__(self, neighbour, is_live, position, charge):
        self.neighbour = neighbour
        self.is_live = is_live
        self.position = position
        self.charge = charge

    def change(self):
        if self.neighbour == 3:
            self.is_live = 1
        elif self.neighbour == 2:
            pass
        else:
            self.is_live = 0

    def convert(self):
        if self.is_live == 0:
            self.is_live = 1
        else:
            self.is_live = 0
