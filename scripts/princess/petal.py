"""A single falling petal shape."""


def petal(x: float, y: float) -> str:
    return f'<path d="M{x} {y} q6 -9 12 0 q-6 9 -12 0 Z"/>'


PETALS = [(120, 0.0, 30), (360, 2.4, -20), (540, 4.8, 25), (260, 7.2, -30), (470, 9.6, 15)]


def petals(p: dict, an) -> str:
    """Petals drift down across the name, one every 2.4 seconds."""
    out = []
    for x, t, drift in PETALS:
        frames = [(0.0, "opacity:0;transform:translate(0,0) rotate(0deg)"), (t, "opacity:0;transform:translate(0,0) rotate(0deg)"),
                  (t + 0.4, "opacity:.9;transform:translate(0,30px) rotate(40deg)"),
                  (t + 3.6, f"opacity:0;transform:translate({drift}px,360px) rotate(260deg)")]
        out.append(f'<g fill="{p["petal"]}" {an.attr(frames, base="opacity:0;")}>{petal(x, -12)}</g>')
    return "".join(out)
