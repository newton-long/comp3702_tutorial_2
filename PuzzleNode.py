# State representation
from __future__ import annotations

import copy
from typing import List


class PuzzleNode:
    def __init__(self, parent: PuzzleNode|None, action, current_state: List):
        self.parent = parent
        self.action = action
        self.current_state = tuple([tuple(row) for row in current_state])

        self.blank_col, self.blank_row = self.find_blank()
        self.last_col = len(current_state) - 1
        self.last_row = len(current_state[0]) - 1

    def find_blank(self):
        for index, row in enumerate(self.current_state):
            if -1 in row:
                return row.index(-1), index

    def actions(self):
        actions = []

        if self.blank_col > 0:
            actions.append('L')
        if self.blank_col < self.last_col:
            actions.append('R')
        if self.blank_row > 0:
            actions.append('U')
        if self.blank_row < self.last_row:
            actions.append('D')

        return actions

    def step(self, action):
        new_state = list(list(row) for row in self.current_state)

        if self.blank_row == 0 and action == 'U' \
            or self.blank_row == self.last_row and action == 'D' \
            or self.blank_col == 0 and action == 'L' \
            or self.blank_col == self.last_col and action == 'R':
            raise Exception('Fell off the grid!')

        if action == 'U':
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row - 1][self.blank_col]
            new_state[self.blank_row - 1][self.blank_col] = -1
        elif action == 'D':
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row + 1][self.blank_col]
            new_state[self.blank_row + 1][self.blank_col] = -1
        elif action == 'L':
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row][self.blank_col - 1]
            new_state[self.blank_row][self.blank_col - 1] = -1
        elif action == 'R':
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row][self.blank_col + 1]
            new_state[self.blank_row][self.blank_col + 1] = -1

        return new_state

    def print(self):
        print(f'Action taken: {self.action}' )
        for row in self.current_state:
            print(' '.join([str(item) for item in row]))
        print("\n")

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
        for command, position in neighbours.items():
            x_new, y_new = position[0], position[1]
            if self.is_valid_pos_2d(x_new, y_new):
                succ_state = copy.deepcopy(self.grid)  # We don't want to ruin the previous state's grid
                i_new = self.to_1d(x_new, y_new)
                succ_state[i_old], succ_state[i_new] = succ_state[i_new], succ_state[i_old]
                succ = Node(succ_state, command, self)
                children.append(succ)

        return children
