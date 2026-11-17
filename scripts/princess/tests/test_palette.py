import re
import unittest

from palette import PALETTES


class PaletteTest(unittest.TestCase):
    def test_themes_share_keys(self):
        self.assertEqual(PALETTES["light"].keys(), PALETTES["dark"].keys())

    def test_colors_are_hex(self):
        for theme in PALETTES.values():
            for color in theme.values():
                self.assertRegex(color, re.compile(r"^#[0-9a-f]{6}$"))


if __name__ == "__main__":
    unittest.main()
