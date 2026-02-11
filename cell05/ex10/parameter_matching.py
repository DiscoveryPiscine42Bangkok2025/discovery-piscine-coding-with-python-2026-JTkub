#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    user_word = input("What was the parameter? ")

    if user_word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
