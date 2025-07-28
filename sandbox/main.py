from puzzle.board import Board

def demo():

    board = Board()

    board.place("Orange", 0, 0)
    board.print()        
    print()

    board.place("Magenta", 0, 0)
    board.print()       
    print()
    
    board.place("Magenta", 0, 3)
    board.print()       
    print()

    removed = board.remove("Orange", 0, 0)
    print("   removed?", removed)
    board.print()
    print()

    removed = board.remove("Magenta", 0, 3)
    print("   removed?", removed)
    board.print()
    print()

    
    for row in range(board.rows):        # 0 .. 4
        for col in range(board.cols):    # 0 .. 10
            board.place("Test", row, col)   # 1 × 1 piece, always legal
            print(f"Placed at ({row}, {col})")
            board.print()                  # show the grid
            print()      

    for row in range(board.rows):        # 0 .. 4
        for col in range(board.cols):    # 0 .. 10
            board.remove("Test", row, col)   # 1 × 1 piece, always legal
            print(f"Placed at ({row}, {col})")
            board.print()                  # show the grid
            print()      

if __name__ == "__main__":
    demo()
