class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['.' for _ in range(cols)] for _ in range(rows)]

    def can_place(self, piece, anchor_row, anchor_col):
        for r_off, c_off in piece:
            r, c = anchor_row + r_off, anchor_col + c_off
            if not (0 <= r < self.rows and 0 <= c < self.cols):
                return False  # out of bounds
            if self.grid[r][c] != '.':
                return False  # spot already taken
        return True

    def place_piece(self, piece, anchor_row, anchor_col, label):
        if not self.can_place(piece, anchor_row, anchor_col):
            return False
        for r_off, c_off in piece:
            self.grid[anchor_row + r_off][anchor_col + c_off] = label
        return True

    def remove_piece(self, piece, anchor_row, anchor_col):
        for r_off, c_off in piece:
            self.grid[anchor_row + r_off][anchor_col + c_off] = '.'

    def print(self):
        for row in self.grid:
            print(' '.join(row))
