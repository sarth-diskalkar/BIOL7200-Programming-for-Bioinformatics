#!/usr/bin/env python3

import sys

def check_paired(string: str) -> None:
    pair_score = 0
    for char in string:
        # If any closing parentheses were seen before an open parenthesis
        if pair_score < 0:
            print("NOT PAIRED")
            return
        
        if char not in {"(", ")"}:
            continue
        if char == "(":
            pair_score += 1
        else:
            pair_score -= 1
    
    # If any parentheses were unpaired
    if pair_score != 0:
        print("NOT PAIRED")
        return

    # Otherwise all were paired
    print("PAIRED")

check_paired(sys.argv[1])
