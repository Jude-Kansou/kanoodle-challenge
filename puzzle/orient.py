# puzzle/orient.py

from typing import List, Tuple, Set
Coord = Tuple[int, int]

def _normalise(pts: List[Coord]) -> Tuple[Coord, ...]:
    min_r = min(r for r, _ in pts)
    min_c = min(c for _, c in pts)
    return tuple(sorted((r - min_r, c - min_c) for r, c in pts))

def generate_orientations(base: List[Coord]):
    # Return (orientations, bounding_boxes)
    seen: Set[Tuple[Coord, ...]] = set()
    orients, boxes = [], []
    for mirror in (0, 1):
        work = [(r, -c) for r, c in base] if mirror else base
        for rot in range(4):          # 0°,90°,180°,270°
            if rot:  # rotate CCW once
                work = [(c, -r) for r, c in work]
            norm = _normalise(work)
            if norm in seen:
                continue
            seen.add(norm)
            orients.append(list(norm))
            h = max(r for r, _ in norm) + 1
            w = max(c for _, c in norm) + 1
            boxes.append((h, w))
    return orients, boxes

# def flip(piece: List[Coord]) -> List[Coord]:
#     c_max = max(c for _, c in piece)          # right-most column
#     return [(r, (-c) + c_max) for r, c in piece]
