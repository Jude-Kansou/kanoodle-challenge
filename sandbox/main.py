# sandbox/main.py

from puzzle.board import Board

def demo():

    b = Board()
    b.place("Orange", 3, 0, 0)   # orient 3
    b.print()
    print()
    b.place("Orange", 0, 2, 2)   # should now be rejected (already placed)
    b.print()
    print()
    b.place("Gray",   0, 2, 5)
    b.print()
    print()

    b.remove("Orange")
    b.print()
    print()


if __name__ == "__main__":
    demo()
