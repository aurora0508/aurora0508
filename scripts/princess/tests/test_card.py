import unittest
import xml.etree.ElementTree as ET

from card import render
from palette import PALETTES

NS = "{http://www.w3.org/2000/svg}"


class CardTest(unittest.TestCase):
    def test_both_themes_are_valid_svg(self):
        for theme, p in PALETTES.items():
            with self.subTest(theme=theme):
                self.assertEqual(ET.fromstring(render(p)).tag, f"{NS}svg")


if __name__ == "__main__":
    unittest.main()
