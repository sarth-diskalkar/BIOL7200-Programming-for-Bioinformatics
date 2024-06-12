#!/usr/bin/env python3
import sys

def check_parenthesis(case: str) -> None:
    open_count = 0
    for char in case:
        if char == "(":
            open_count += 1
        elif char == ")":
            open_count -= 1
            if open_count < 0:
                print("NOT PAIRED")
                return
    if open_count == 0:
        print("PAIRED")
    else:
        print("NOT PAIRED")
check_parenthesis(sys.argv[1])















