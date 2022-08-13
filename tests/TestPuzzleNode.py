import unittest

from PuzzleNode import PuzzleNode, LEFT, UP, RIGHT, DOWN


class TestPuzzleNode(unittest.TestCase):
    def setUp(self) -> None:
        self.bottom_left = PuzzleNode(None, None, (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        ))

    def test_find_blank(self):
        self.assertEqual((2, 2), self.bottom_left.find_blank())

    def test_find_blank_not_equal(self):
        node = PuzzleNode(None, None, (
            (1, -1, 3),
            (4, 5, 6),
            (7, 8, 2)
        ))
        self.assertEqual((0, 1), node.find_blank())

    def test_find_actions_bottom_right(self):
        self.assertEqual(
            [LEFT, UP],
            self.bottom_left.actions()
        )

    def test_find_actions_top_left(self):
        node = PuzzleNode(None, None, (
            (-1, 2, 3),
            (4, 5, 6),
            (7, 8, 1)
        ))
        self.assertEqual(
            [RIGHT, DOWN],
            node.actions()
        )

    def test_find_actions_center(self):
        node = PuzzleNode(None, None, (
            (5, 2, 3),
            (4, -1, 6),
            (7, 8, 1)
        ))
        self.assertEqual(
            [LEFT, RIGHT, UP, DOWN],
            node.actions()
        )

    def test_step_off_grid(self):
        node = PuzzleNode(None, None, (
            (-1, 2, 3),
            (4, 5, 6),
            (7, 8, 1)
        ))
        with self.assertRaises(Exception):
            node.step(UP)

    def test_step_up(self):
        node = PuzzleNode(None, None, (
            (5, 2, 3),
            (4, -1, 6),
            (7, 8, 1)
        ))
        self.assertEqual(
            (
                (5, -1, 3),
                (4, 2, 6),
                (7, 8, 1)
            ),
            node.step(UP)
        )

    def test_step_down(self):
        node = PuzzleNode(None, None, (
            (5, 2, 3),
            (4, -1, 6),
            (7, 8, 1)
        ))
        self.assertEqual(
            (
                (5, 2, 3),
                (4, 8, 6),
                (7, -1, 1)
            ),
            node.step(DOWN)
        )

    def test_step_left(self):
        node = PuzzleNode(None, None, (
            (5, 2, 3),
            (4, -1, 6),
            (7, 8, 1)
        ))
        self.assertEqual(
            (
                (5, 2, 3),
                (-1, 4, 6),
                (7, 8, 1)
            ),
            node.step(LEFT)
        )

    def test_step_right(self):
        node = PuzzleNode(None, None, (
            (5, 2, 3),
            (4, -1, 6),
            (7, 8, 1)
        ))
        self.assertEqual(
            (
                (5, 2, 3),
                (4, 6, -1),
                (7, 8, 1)
            ),
            node.step(RIGHT)
        )

    def test_tuple_equality(self):
        t1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        t2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

        self.assertTrue(t1 == t2)

    def test_less_than(self):
        cost1 = PuzzleNode(None, UP, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))
        cost2 = PuzzleNode(None, DOWN, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))
        cost3 = PuzzleNode(None, LEFT, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))
        cost4 = PuzzleNode(None, RIGHT, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))

        self.assertLess(cost1, cost2)
        self.assertLess(cost2, cost3)
        self.assertLess(cost3, cost4)