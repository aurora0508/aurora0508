"""A four-pointed sparkle."""


def star(x: float, y: float, r: float) -> str:
    k = r * 0.28
    return (f'<path d="M{x} {y - r} Q{x + k} {y - k} {x + r} {y} Q{x + k} {y + k} {x} {y + r} '
            f'Q{x - k} {y + k} {x - r} {y} Q{x - k} {y - k} {x} {y - r} Z"/>')
