#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    for n in range(11):
        line = f"Table de {n}:"
        for i in range(11):
            line += f" {n * i}"
        print(line)
