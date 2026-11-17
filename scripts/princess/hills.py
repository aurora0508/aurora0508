"""Rolling hills behind and in front of the castle."""

from anims import Anims

H = 360


def hills_back(p: dict, an: Anims) -> str:
    return f'<path d="M560 {H} C700 268 820 262 940 286 S1140 262 1200 276 V{H} Z" fill="{p["hill"]}"/>'


def hills_front(p: dict, an: Anims) -> str:
    return f'<path d="M520 {H} C640 300 780 316 900 330 S1120 312 1200 320 V{H} Z" fill="{p["hill"]}" opacity=".8"/>'
