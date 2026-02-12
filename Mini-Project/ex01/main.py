from checkmate import *
from os.path import isfile
import sys

def main():
    argv = sys.argv 
    argv.pop(0)
    argc = len(argv)
    if argc > 0: 
        for board in argv:
            if isfile(board):
                with open(board) as file:
                    checkmate(file.read())

if __name__ == "__main__":
    main()