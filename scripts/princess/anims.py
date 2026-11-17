"""CSS keyframes on one shared clock.

GitHub shows the banner through <img>, so all motion is CSS. Every animated
element also gets a static style, which is what viewers with
prefers-reduced-motion see.
"""

CYCLE = 12.0


class Anims:
    def __init__(self) -> None:
        self.rules: list[str] = []

    def attr(self, frames: list[tuple[float, str]], base: str = "", cls: str = "") -> str:
        frames = sorted(frames)
        if frames[0][0] > 0:
            frames.insert(0, (0.0, frames[0][1]))
        if frames[-1][0] < CYCLE:
            frames.append((CYCLE, frames[-1][1]))
        name = f"k{len(self.rules)}"
        body = " ".join(f"{t / CYCLE * 100:.3f}% {{ {css} }}" for t, css in frames)
        self.rules.append(f"@keyframes {name} {{ {body} }}")
        return f'class="{" ".join(c for c in ("a", cls) if c)}" style="{base}animation-name:{name};"'
