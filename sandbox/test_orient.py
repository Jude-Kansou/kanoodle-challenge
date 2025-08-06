# sandbox/main.py

from puzzle.orient import generate_orientations, flip, _normalise
from puzzle.pieces import PIECES

def test_flip_vs_builtin():
    for name, coords in PIECES.items():
        # generate one flipped pose via your helper
        flipped = _normalise(flip(coords))

        # run orientation generator
        orients, _ = generate_orientations(coords)

        found = any(_normalise(o) == flipped for o in orients)
        print(f"{name:7s}  flip-included?  {found}")

if __name__ == "__main__":
    test_flip_vs_builtin()
