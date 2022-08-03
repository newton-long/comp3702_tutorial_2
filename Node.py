# State representation
import copy


class Node:
    def __init__(self, grid, previous_action, parent):
        self.grid = grid
        self.previous_action = previous_action
        self.parent = parent
        self.total_cost = 0 # For UCS

    @staticmethod
    def to_1d(x, y):
        return (3 * y) + x

    @staticmethod
    def to_2d(i):
        return i % 3, i // 3

    @staticmethod
    def is_valid_pos_2d(x, y):
        return 0 <= x and x < 3 and 0 <= y and y < 3

    # Override equality and hash - needed to check when 2 states are equal
    # It would otherwise default to checking object references
    def __eq__(self, other):
        return self.grid == other.grid

    def __hash__(self):
        return hash(tuple(self.grid))

    def print(self, description):
        print(description)
        for y in range(3):
            for x in range(3):
                print("{:^3}".format(str(self.grid[self.to_1d(x, y)])), end='')
            print()
        print()

    def get_blank_i(self):
        return self.grid.index("_")

    @staticmethod
    def get_blank_tile_neighbours(x, y):
        """
        Takes blank tile coordinates and for every action in A returns where it would go.
        """
        return {'L': (x - 1, y),
                'R': (x + 1, y),
                'U': (x, y - 1),
                'D': (x, y + 1)}

    def get_children(self):
        # Current blank tile location
        i_old = self.get_blank_i()
        x_old, y_old = self.to_2d(i_old)

        # Neighbouring blank tile locations
        neighbours = self.get_blank_tile_neighbours(x_old, y_old)

        # For valid neighbouring positions, swap the tiles around
        children = list()
        for a, n in neighbours.items():
            x_new, y_new = n[0], n[1]
            if self.is_valid_pos_2d(x_new, y_new):
                succ_state = copy.deepcopy(self.grid)  # We don't want to ruin the previous state's grid
                i_new = self.to_1d(x_new, y_new)
                succ_state[i_old], succ_state[i_new] = succ_state[i_new], succ_state[i_old]
                succ = Node(succ_state, a, self)
                children.append(succ)

        return children
