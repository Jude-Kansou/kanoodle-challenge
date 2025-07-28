# puzzle/board.py
# Lightweight 11 × 5 board to host Kanoodle pieces.

from typing import Iterable, List, Tuple
from puzzle.piece import Piece          # dataclass
from puzzle.pieces import PIECES        # raw dict

Coord = Tuple[int, int]   


class Board:
    EMPTY = "."                

    def __init__(self, rows: int = 5, cols: int = 11) -> None:
        self.rows = rows
        self.cols = cols
        self.grid: List[List[str]] = [[self.EMPTY] * cols for _ in range(rows)]

        
        self.pieces: dict[str, Piece] = {
            name: Piece(name, coords, name[0].upper())
            for name, coords in PIECES.items()
        }

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

    def place(self, name: str, row: int, col: int) -> bool:
        p = self.pieces[name]
        success = self._place_piece(p.coords, row, col, p.label)

        if not success:   # ← 4‑line addition starts here
            print(
                f"Cannot place {name} at ({row}, {col}): "
                "square out‑of‑bounds or already occupied.\n"
            )
        return success 
    

    def remove(self, name: str, row: int, col: int) -> bool:
        """
        High‑level helper. Returns True if the piece was removed,
        False if the piece wasn't found at that anchor. All safety
        logic—including the try/except we added—is still inside remove_piece.
        """
        p = self.pieces[name]         
        return self._remove_piece(p, row, col)

    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self.grid)

    def print(self) -> None:  \
        print(self.__str__())
