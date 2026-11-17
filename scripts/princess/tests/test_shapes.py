import unittest

from palette import PALETTES
from ribbon import ROLE, role
from star import star
from tower import tower

P = PALETTES["light"]


class ShapesTest(unittest.TestCase):
    def test_star_is_a_closed_path(self):
        self.assertTrue(star(10, 10, 5).endswith('Z"/>'))

    def test_tower_has_a_lit_window(self):
        self.assertIn(P["window"], tower(100, 300, 30, 100, 40, P))

    def test_ribbon_carries_her_role(self):
        self.assertIn(ROLE, role(P, None))


if __name__ == "__main__":
    unittest.main()
