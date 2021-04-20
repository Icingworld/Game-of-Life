from cell import Cell

cell_list = []


class Rule:
    def __init__(self, width, height, wow, state):
        self.width = width
        self.height = height
        self.wow = wow
        self.state = state

    def run(self):
        for i in range(0, self.width//self.wow):
            for j in range(0, self.height//self.wow):
                new_cell = Cell(0, 0, (i, j), 0)
                cell_list.append(new_cell)

    @staticmethod
    def get_neighbour():
        for cell in cell_list:
            cell.neighbour = 0
            x = cell.position[0] - 1
            y = cell.position[1] - 1
            for i in range(0, 3):
                for j in range(0, 3):
                    if (i, j) != (1, 1):
                        for cell2 in cell_list:
                            if cell2.position == (x + i, y + j):
                                if cell2.is_live == 1:
                                    cell.neighbour = cell.neighbour + 1
