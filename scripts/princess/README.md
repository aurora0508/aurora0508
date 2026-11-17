# princess

Draws the profile banner (`assets/banner-light.svg`, `assets/banner-dark.svg`)
and the chapter divider (`assets/divider.svg`). Standard library only.

```bash
python3 scripts/princess                                                     # redraw
PYTHONPATH=scripts/princess python3 -m unittest discover -s scripts/princess/tests
```

`card.py` stacks the layers in `LAYERS` from back to front: moon, hills,
castle, stars, petals, the wand trail, the words, the ribbon and the tiara.
Each layer is a function `(palette, anims) -> svg` in its own module, so a new
layer is one module and one line in `LAYERS`.

CI fails when the SVGs in `assets/` don't match the code, so redraw before you
commit.
