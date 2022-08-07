import unittest

from node_utils import get_inversion_count


class TestNodeUtils(unittest.TestCase):
    def test_odd_parity(self):
        init_state = (1, 2, 3, 4, 5, 6, 8, 7)
        self.assertEqual(1, get_inversion_count(init_state))

    def test_even_parity(self):
        init_state = (7, 2, 4, 5, -1, 6, 8, 3, 1)
        self.assertEqual(0, get_inversion_count(init_state) % 2)
        self.assertEqual(16, get_inversion_count(init_state))

