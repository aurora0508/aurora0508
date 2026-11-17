"""A small gold tiara that floats over her name."""

from anims import Anims


def tiara(x: float, y: float, p: dict) -> str:
    """A small tiara: five peaks with jewels on a curved band."""
    pts = []
    for i in range(9):
        px = x - 48 + i * 12
        py = y - (22 if i == 4 else 15 if i in (2, 6) else 9 if i % 2 == 0 else 2)
        pts.append(f"{px} {py}")
    band = f'M{x - 52} {y + 6} Q{x} {y - 6} {x + 52} {y + 6}'
    return (f'<path d="M{x - 48} {y} L{" L".join(pts)} L{x + 48} {y} Q{x} {y - 8} {x - 48} {y} Z" fill="{p["gold"]}" stroke="{p["gold_hi"]}" stroke-width="1.2" stroke-linejoin="round"/>'
            f'<path d="{band}" fill="none" stroke="{p["gold"]}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y - 16}" r="4.5" fill="{p["flag"]}"/>'
            f'<circle cx="{x - 24}" cy="{y - 9}" r="3" fill="{p["ribbon"]}"/><circle cx="{x + 24}" cy="{y - 9}" r="3" fill="{p["ribbon"]}"/>')


def crown(p: dict, an: Anims) -> str:
    float_ = [(k * 1.5, f"transform:translateY({(0, -3)[k % 2]}px)") for k in range(9)]
    return f'<g {an.attr(float_, base="")}>{tiara(250, 104, p)}</g>'
