# puzzle/board.py
# Lightweight 11 × 5 board to host Kanoodle pieces.

from typing import Iterable, List, Tuple
from puzzle.piece import Piece          # dataclass
from puzzle.pieces import PIECES        # raw dict
from puzzle.orient import generate_orientations
Coord = Tuple[int, int]   


class Board:
    EMPTY = "."                

    def __init__(self, rows: int = 5, cols: int = 11) -> None:
        self.rows = rows
        self.cols = cols
        self.grid: List[List[str]] = [[self.EMPTY] * cols for _ in range(rows)]

        self.pieces: dict[str, Piece] = {}

        for pid, (name, coords) in enumerate(sorted(PIECES.items())):
            label = name[0].upper()
            size  = len(coords)

            # create frozen Piece with empty orientation fields
            p = Piece(pid, name, label, size, coords)

            # generate unique poses once
            oris, boxes = generate_orientations(coords)
            object.__setattr__(p, "orientations", oris)
            object.__setattr__(p, "bounding_boxes", boxes)

            self.pieces[name] = p

        self.placed: dict[str, Tuple[int,int,int]] = {}

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self.grid)

    def print(self) -> None:  \
        print(self.__str__())

    def _cells(self, piece: Iterable[Coord], anchor_row: int, anchor_col: int) -> List[Coord]:
        return [(anchor_row + r_off, anchor_col + c_off) for r_off, c_off in piece]

    def can_place(self, piece: Iterable[Coord], anchor_row: int, anchor_col: int) -> bool:
        for r, c in self._cells(piece, anchor_row, anchor_col):
            if not (0 <= r < self.rows and 0 <= c < self.cols):
                return False
            if self.grid[r][c] != self.EMPTY:
                return False
        return True
    
    def _place_piece(
        self, piece: Iterable[Coord], anchor_row: int, anchor_col: int, label: str
    ) -> bool:
        cells = self._cells(piece, anchor_row, anchor_col)
        if any(
            not (0 <= r < self.rows and 0 <= c < self.cols) or self.grid[r][c] != self.EMPTY
            for r, c in cells
        ):
            return False

        for r, c in cells:
            self.grid[r][c] = label
        return True
    
    def place(self, name: str, orient_id: int, row: int, col: int) -> bool:
        p = self.pieces[name]

        # ---- sanity checks -----------------------------------------------------
        if name in self.placed:
            print(f"{name} is already on the board.")
            return False
        if orient_id >= len(p.orientations):
            print(f"{name} has no orientation #{orient_id}.")
            return False

        # ---- quick out-of-bounds via bounding box -----------------------------
        h, w = p.bounding_boxes[orient_id]
        if row + h > self.rows or col + w > self.cols:
            print(f"{name}[{orient_id}] at ({row},{col}) exceeds board.")
            return False

        # ---- collision check & actual placement --------------------------------
        ok = self._place_piece(p.orientations[orient_id], row, col, p.label)
        if ok:
            self.placed[name] = (orient_id, row, col)   # remember pose
        else:
            print(f"Collision when placing {name}[{orient_id}] at ({row},{col}).")
        return ok

    def remove(self, name: str) -> bool:
        if name not in self.placed:
            print(f"{name} is not on the board.")
            return False

        orient_id, row, col = self.placed.pop(name)
        p       = self.pieces[name]
        coords  = p.orientations[orient_id]

        cells = [(row + r, col + c) for r, c in coords]
        # validate
        if any(self.grid[r][c] != p.label for r, c in cells):
            print("Board desync detected; removal aborted.")
            return False
        # clear
        for r, c in cells:
            self.grid[r][c] = self.EMPTY
        return True

"""

This is the stuff I wrote for iteration one I wanted to keep for later reference

def _remove_piece(self, piece: Piece, anchor_row: int, anchor_col: int) -> bool:
    cells = [(anchor_row + r_off, anchor_col + c_off) for r_off, c_off in piece.coords]

    try:
        
        for r, c in cells:
            if self.grid[r][c] == self.EMPTY:
                raise AssertionError
        
        for r, c in cells:
            self.grid[r][c] = self.EMPTY
        return True

    except AssertionError:
        print(
            f"The {piece.name} piece at anchor ({anchor_row}, {anchor_col}) "
            "was not found; board left unchanged.\n"
        )
        return False


def legacy_place(self, name: str, row: int, col: int) -> bool:
    p = self.pieces[name]
    success = self._place_piece(p.coords, row, col, p.label)

    if not success:   # ← 4‑line addition starts here
        print(
            f"Cannot place {name} at ({row}, {col}): "
            "square out‑of‑bounds or already occupied.\n"
        )
    return success 


def legacy_remove(self, name: str, row: int, col: int) -> bool:

    # High‑level helper. Returns True if the piece was removed,
    # False if the piece wasn't found at that anchor. All safety
    # logic—including the try/except we added—is still inside remove_piece.
    
    p = self.pieces[name]         
    return self._remove_piece(p, row, col)
"""