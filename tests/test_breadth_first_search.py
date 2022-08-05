import unittest

from breadth_first_search import breadth_first_search


class TestBreadthFirstSearch(unittest.TestCase):
    def test_one_step(self):
        start = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
        ]
        goal = [
            [1, 2, 3],
            [4, 5, 6],
            [7, -1, 8]
        ]

        steps = breadth_first_search(start, goal)
        self.assertEqual(2, len(steps) )

    def test_two_steps(self):
        start = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
        ]
        goal = [
            [1, 2, 3],
            [4, 5, 6],
            [-1, 7, 8]
        ]

        steps = breadth_first_search(start, goal)
        self.assertEqual(3, len(steps))

    def test_move_up(self):
        start = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
        ]
        goal = [
            [1, 2, 3],
            [4, 5, -1],
            [7, 8, 6]
        ]

        steps = breadth_first_search(start, goal)
        self.assertEqual(2, len(steps))

    def test_hard(self):
        init_state = [
            [7, 2, 4],
            [5, 3, 6],
            [8, -1, 1]
        ]
        goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
        ]
        steps = breadth_first_search(init_state, goal_state)
        self.assertEqual(20, len(steps))
