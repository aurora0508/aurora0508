"""The words on the banner."""

from anims import Anims


def masthead(p: dict, an: Anims) -> str:
    return ('<text x="64" y="58" class="kicker">ONCE UPON A HEADLINE</text>'
            '<text x="60" y="222" class="mast">aurora</text>')


def tagline(p: dict, an: Anims) -> str:
    return '<text x="80" y="326" class="tagline">writing the stories behind the stars, happily ever after</text>'
