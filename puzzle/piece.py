# puzzle/piece.py
from dataclasses import dataclass, field
from typing import List, Tuple

Coord = Tuple[int, int]

@dataclass(frozen=True)
class Piece:
    piece_id: int
    name: str
    label: str
    size: int                     # len(coords)
    coords: List[Coord]
    
    orientations: List[List[Coord]]          = field(default_factory=list, repr=False, compare=False)
    bounding_boxes: List[Tuple[int, int]]    = field(default_factory=list, repr=False, compare=False)


