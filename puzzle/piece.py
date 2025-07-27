# puzzle/piece.py
from dataclasses import dataclass
from typing import List, Tuple

Coord = Tuple[int, int]

@dataclass(frozen=True)
class Piece:
    name: str
    coords: List[Coord]
    label: str