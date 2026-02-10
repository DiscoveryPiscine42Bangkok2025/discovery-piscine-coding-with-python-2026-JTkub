#!/usr/bin/env python3

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))

print("Thank you!")

operations = [
    ("+", first + second),
    ("-", first - second),
    ("/", first // second),
    ("*", first * second)
]

for op, result in operations:
    if op == "-":
        print(f"{first}- {second} = {result}")
    else:
        print(f"{first} {op} {second} = {result}")
