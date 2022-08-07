import unittest

from breadth_first_search import breadth_first_search


class TestBreadthFirstSearch(unittest.TestCase):
    def test_one_step(self):
        start = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )
        goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, -1, 8)
        )

        steps = breadth_first_search(start, goal)
        self.assertEqual(2, len(steps) )

    def test_two_steps(self):
        start = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )
        goal = (
            (1, 2, 3),
            (4, 5, 6),
            (-1, 7, 8)
        )

        steps = breadth_first_search(start, goal)
        self.assertEqual(3, len(steps))

    def test_move_up(self):
        start = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )
        goal = (
            (1, 2, 3),
            (4, 5, -1),
            (7, 8, 6)
        )

        steps = breadth_first_search(start, goal)
        self.assertEqual(2, len(steps))

    def test_hard(self):
        init_state = (
            (7, 2, 4),
            (5, 3, 6),
            (8, -1, 1)
        )
        goal_state = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )
        steps = breadth_first_search(init_state, goal_state)
        self.assertEqual(20, len(steps))

    def test_tutorial2a(self):
        init_state = (
            (1, 3, 4,),
            (8, 6, 2),
            (7, -1, 5)
        )
        goal_state = (
            (1, 2, 3),
            (8, -1, 4),
            (7, 6, 5)
        )
        steps = breadth_first_search(init_state, goal_state)
        self.assertEqual(6, len(steps))

    def test_tutorial2b(self):
        init_state = (
            (2, 8, 1),
            (-1, 4, 3),
            (7, 6, 5)
        )
        goal_state = (
            (1, 2, 3),
            (8, -1, 4),
            (7, 6, 5)
        )
        steps = breadth_first_search(init_state, goal_state)
        self.assertEqual(10, len(steps))

    def test_tutorial2c(self):
        init_state = (
            (2, 8, 1),
            (4, 6, 3),
            (-1, 7, 5)
        )
        goal_state = (
            (1, 2, 3),
            (8, -1, 4),
            (7, 6, 5)
        )
        steps = breadth_first_search(init_state, goal_state)
        self.assertEqual(13, len(steps))

    def test_unsolvable(self):
        init_state = (
            (1, 2, 3),
            (4, 5, 6),
            (-1, 8, 7)
        )
        goal_state = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )

        steps = breadth_first_search(init_state, goal_state)
        self.assertEqual(0, len(steps))
