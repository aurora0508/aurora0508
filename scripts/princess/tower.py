"""One storybook castle tower."""


def tower(x: float, base: float, w: float, h: float, roof: float, p: dict) -> str:
    """One castle tower: a wall, a cone roof with a pennant, and a lit arched window."""
    top = base - h
    win = (f'<path d="M{x - w * 0.14} {top + h * 0.42} v{-h * 0.1} a{w * 0.14} {w * 0.14} 0 0 1 {w * 0.28} 0 '
           f'v{h * 0.1} Z" fill="{p["window"]}"/>')
    return (f'<rect x="{x - w / 2}" y="{top}" width="{w}" height="{h}" fill="{p["castle"]}" stroke="{p["castle_edge"]}" stroke-width="1.5"/>'
            f'<path d="M{x - w / 2 - 5} {top} L{x} {top - roof} L{x + w / 2 + 5} {top} Z" fill="{p["roof"]}" stroke="{p["castle_edge"]}" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<line x1="{x}" y1="{top - roof}" x2="{x}" y2="{top - roof - 16}" stroke="{p["castle_edge"]}" stroke-width="1.5"/>'
            f'<path d="M{x} {top - roof - 16} l12 4 l-12 4 Z" fill="{p["flag"]}"/>' + win)
