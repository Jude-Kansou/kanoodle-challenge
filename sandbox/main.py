from puzzle.board import Board

def demo():
    board = Board()

    board.place("Orange", 0, 0)
    board.print()        # or:  print(board)
    print()


    success = board.place("Red", 1, 5)
    print("   placed?" , success)
    board.print()
    print()

    # removed = board.remove("Red", , 1)
    # print("   removed?", removed)
    # board.print()
    # print()

    removed = board.remove("Orange", 0, 0)
    print("   removed?", removed)
    board.print()
    print()

if __name__ == "__main__":
    demo()
