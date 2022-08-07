# State representation
from __future__ import annotations

import copy
from typing import List

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

actions = {
    LEFT: 'L',
    RIGHT: 'R',
    UP: 'U',
    DOWN: 'D'
}


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
            actions.append(LEFT)
        if self.blank_col < self.last_col:
            actions.append(RIGHT)
        if self.blank_row > 0:
            actions.append(UP)
        if self.blank_row < self.last_row:
            actions.append(DOWN)

        return actions

    def step(self, action):
        new_state = list(list(row) for row in self.current_state)

        if self.blank_row == 0 and action == UP \
            or self.blank_row == self.last_row and action == DOWN \
            or self.blank_col == 0 and action == LEFT \
            or self.blank_col == self.last_col and action == RIGHT:
            raise Exception('Fell off the grid!')

        if action == UP:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row - 1][self.blank_col]
            new_state[self.blank_row - 1][self.blank_col] = -1
        elif action == DOWN:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row + 1][self.blank_col]
            new_state[self.blank_row + 1][self.blank_col] = -1
        elif action == LEFT:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row][self.blank_col - 1]
            new_state[self.blank_row][self.blank_col - 1] = -1
        elif action == RIGHT:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row][self.blank_col + 1]
            new_state[self.blank_row][self.blank_col + 1] = -1

        return new_state

    def print(self):
        print(f'Action taken: {actions[self.action]}' )
        for row in self.current_state:
            print(' '.join([str(item) for item in row]))
        print("\n\n")

