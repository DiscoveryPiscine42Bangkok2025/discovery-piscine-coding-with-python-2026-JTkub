from checkmate import *

# def main():
#     board = """
#     R...
#     .K..
#     ..P.
#     ....
#     """
#     checkmate(board)

def main():
    boards = [
"""\
R...
.K..
..P.
....\
""",

"""\
..
.K\
""",

"""\
B...
.K..
....
....\
""",

"""\
Q...
.K..
....
....\
""",

"""\
....
.P..
.K..
....\
""",

"""\
....
.P..
K...
....\
""",

"""\
.k..
.P..
....
....\
"""
    ]
    for i, board in enumerate(boards, start=1):
        checkmate(board)


if __name__ == "__main__":
    main()