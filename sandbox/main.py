"""
Scratch space for trying ideas.
Run with:  python -m sandbox.main
"""

from puzzle.board import Board
from puzzle.pieces import PIECES

def demo():
    board = Board()
    orange = PIECES["Orange"]
    board.place_piece(orange, 0, 0, "O")
    print(board, "\n")          # shows grid with an 'O' shape
    board.remove_piece(orange, 0, 0)
    print(board)                # empty again

if __name__ == "__main__":
    demo()
