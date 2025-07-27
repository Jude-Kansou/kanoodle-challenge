from puzzle.pieces import PIECES

EXPECTED_SIZE = {
    "Orange": 4, "Red": 5, "Purple": 5, "Magenta": 5,
    "Green": 5, "Cyan": 5, "Yellow": 5, "Blue": 5,
    "Gray": 5, "Pink": 5, "White": 3, "Grass": 4,
}

def test_bead_counts():
    for name, coords in PIECES.items():
        assert len(coords) == EXPECTED_SIZE[name], f"{name} bead‑count mismatch"

def test_min_coords_non_negative():
    for name, coords in PIECES.items():
        xs, ys = zip(*coords)
        assert min(xs) >= 0 and min(ys) >= 0, f"{name} has negative coord; shift or change convention"

# OPTIONAL – keep only if you insist that (0,0) is part of every shape
def test_contains_origin():
    for name, coords in PIECES.items():
        assert (0, 0) in coords, f"{name} missing (0,0)"
