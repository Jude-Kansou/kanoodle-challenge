# puzzle/board.py
"""Lightweight 11 × 5 board to host Kanoodle pieces."""

from typing import Iterable, List, Tuple

Coord = Tuple[int, int]        # (row, col)


class Board:
    EMPTY = "."                

    def __init__(self, rows: int = 5, cols: int = 11) -> None:
        self.rows = rows
        self.cols = cols
        self.grid: List[List[str]] = [[self.EMPTY] * cols for _ in range(rows)]

    def _cells(self, piece: Iterable[Coord], anchor_row: int, anchor_col: int) -> List[Coord]:
        return [(anchor_row + r_off, anchor_col + c_off) for r_off, c_off in piece]

    def can_place(self, piece: Iterable[Coord], anchor_row: int, anchor_col: int) -> bool:
        for r, c in self._cells(piece, anchor_row, anchor_col):
            if not (0 <= r < self.rows and 0 <= c < self.cols):
                return False
            if self.grid[r][c] != self.EMPTY:
                return False
        return True


    def place_piece(
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

    def remove_piece(self, piece: Iterable[Coord], anchor_row: int, anchor_col: int) -> None:

        for r, c in self._cells(piece, anchor_row, anchor_col):
            assert self.grid[r][c] != self.EMPTY, "Attempted to remove from an empty square"
            self.grid[r][c] = self.EMPTY


    def __str__(self) -> str:
        return "\n".join(" ".join(row) for row in self.grid)

    def print(self) -> None:  # keep your original helper for convenience
        print(self.__str__())
