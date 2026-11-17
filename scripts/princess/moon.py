"""A full moon over the castle."""

from anims import Anims


def moon(p: dict, an: Anims) -> str:
    return f'<circle cx="1120" cy="96" r="30" fill="{p["moon"]}" opacity=".9"/>'
