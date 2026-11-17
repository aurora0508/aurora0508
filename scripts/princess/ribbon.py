"""A banner ribbon with notched tails, carrying her role."""

from anims import Anims

ROLE = "娛樂編輯 · Entertainment Editor, ELLE Taiwan"


def ribbon(x: float, y: float, w: float, text: str, p: dict) -> str:
    h = 34
    return (f'<path d="M{x - 26} {y + 8} h30 v{h} h-30 l12 {-h / 2} Z" fill="{p["ribbon_dark"]}"/>'
            f'<path d="M{x + w + 26} {y + 8} h-30 v{h} h30 l-12 {-h / 2} Z" fill="{p["ribbon_dark"]}"/>'
            f'<path d="M{x} {y} Q{x + w / 2} {y - 10} {x + w} {y} v{h} Q{x + w / 2} {y + h - 10} {x} {y + h} Z" fill="{p["ribbon"]}"/>'
            f'<text x="{x + w / 2}" y="{y + 22}" class="role" text-anchor="middle">{text}</text>')


def role(p: dict, an: Anims) -> str:
    return ribbon(80, 252, 420, ROLE, p)
