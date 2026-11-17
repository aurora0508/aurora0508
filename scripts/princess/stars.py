"""Stars that twinkle twice per cycle, each on its own beat."""

from anims import CYCLE, Anims
from star import star

STARS = [(640, 46, 7, 0.0), (712, 92, 5, 1.2), (842, 40, 6, 2.4), (968, 70, 8, 3.6), (1104, 38, 6, 4.8),
         (1160, 110, 5, 6.0), (590, 130, 5, 7.2), (60, 40, 7, 8.4), (520, 312, 6, 9.6)]


def stars(p: dict, an: Anims) -> str:
    out = []
    for x, y, r, t in STARS:
        frames = []
        for k in range(2):
            t0 = (t + k * 6.0) % CYCLE
            frames += [(t0, "opacity:.3;transform:scale(.6)"), (t0 + 0.5, "opacity:1;transform:scale(1.2)"),
                       (t0 + 1.3, "opacity:.3;transform:scale(.6)")]
        out.append(f'<g fill="{p["star"]}" {an.attr(frames, base="opacity:.8;", cls="fb")}>{star(x, y, r)}</g>')
    return "".join(out)
