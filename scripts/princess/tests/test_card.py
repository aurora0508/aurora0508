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

    def test_title_and_description_for_screen_readers(self):
        root = ET.fromstring(render(PALETTES["light"]))
        self.assertEqual(root.find(f"{NS}title").text, "aurora")
        self.assertIn("Entertainment editor at ELLE Taiwan", root.find(f"{NS}desc").text)

    def test_reduced_motion_stops_animation(self):
        self.assertIn("prefers-reduced-motion", render(PALETTES["dark"]))


if __name__ == "__main__":
    unittest.main()
