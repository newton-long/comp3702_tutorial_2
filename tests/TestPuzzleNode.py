import unittest

from PuzzleNode import Node, PuzzleNode


class TestPuzzleNode(unittest.TestCase):
    def test_find_empty(self):
        node = PuzzleNode(None, None, [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
        ])
        self.assertEqual((2, 2), node.find_blank())

    def test_find_actions_bottom_right(self):
        node = PuzzleNode(None, None, [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, -1]
        ])
        self.assertEqual(
            ['L', 'U'],
            node.actions()
        )

    def test_find_actions_top_left(self):
        node = PuzzleNode(None, None, [
            [-1, 2, 3],
            [4, 5, 6],
            [7, 8, 1]
        ])
        self.assertEqual(
            ['R', 'D'],
            node.actions()
        )

    def test_find_actions_center(self):
        node = PuzzleNode(None, None, [
            [5, 2, 3],
            [4, -1, 6],
            [7, 8, 1]
        ])
        self.assertEqual(
            ['L', 'R', 'U', 'D'],
            node.actions()
        )

    def test_step_off_grid(self):
        node = PuzzleNode(None, None, [
            [-1, 2, 3],
            [4, 5, 6],
            [7, 8, 1]
        ])
        with self.assertRaises(Exception):
            node.step('U')

    def test_step_up(self):
        node = PuzzleNode(None, None, [
            [5, 2, 3],
            [4, -1, 6],
            [7, 8, 1]
        ])
        self.assertEqual(
            [
                [5, -1, 3],
                [4, 2, 6],
                [7, 8, 1]
            ],
            node.step('U')
        )

    def test_step_down(self):
        node = PuzzleNode(None, None, [
            [5, 2, 3],
            [4, -1, 6],
            [7, 8, 1]
        ])
        self.assertEqual(
            [
                [5, 2, 3],
                [4, 8, 6],
                [7, -1, 1]
            ],
            node.step('D')
        )

    def test_step_left(self):
        node = PuzzleNode(None, None, [
            [5, 2, 3],
            [4, -1, 6],
            [7, 8, 1]
        ])
        self.assertEqual(
            [
                [5, 2, 3],
                [-1, 4, 6],
                [7, 8, 1]
            ],
            node.step('L')
        )

    def test_step_right(self):
        node = PuzzleNode(None, None, [
            [5, 2, 3],
            [4, -1, 6],
            [7, 8, 1]
        ])
        self.assertEqual(
            [
                [5, 2, 3],
                [4, 6, -1],
                [7, 8, 1]
            ],
            node.step('R')
        )

    def test_tuple_equality(self):
        t1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        t2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

        self.assertTrue(t1 == t2)