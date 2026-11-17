import unittest

from anims import Anims


class AnimsTest(unittest.TestCase):
    def test_keyframes_span_the_whole_cycle(self):
        an = Anims()
        an.attr([(2.0, "opacity:1")])
        self.assertIn("0.000% { opacity:1 }", an.rules[0])
        self.assertIn("100.000% { opacity:1 }", an.rules[0])

    def test_static_style_comes_first(self):
        attr = Anims().attr([(1.0, "opacity:0")], base="opacity:1;", cls="fb")
        self.assertEqual(attr, 'class="a fb" style="opacity:1;animation-name:k0;"')

    def test_each_animation_gets_its_own_name(self):
        an = Anims()
        an.attr([(1.0, "opacity:0")])
        an.attr([(1.0, "opacity:0")])
        self.assertEqual(len({rule.split()[1] for rule in an.rules}), 2)


if __name__ == "__main__":
    unittest.main()
