#!/usr/bin/env python3

import sys

def calc_dims(height: int) -> list[int]:
    """Given a triangle height, calculate the number of units height per line
    
    Args:
        height:
            The number of lines tall that the triangle will be
    
    returns:
        The number of characters per line for the triangle
    """
    midpoint = -(-height//2) # round up
    dims = [i for i in range(1, midpoint + 1)]
    if height % 2 == 0: # even
        dims += dims[::-1]
    else: # odd
        dims += dims[-2::-1] 
    return dims


def print_triangle(char: str, height: int) -> None:
    """Print a triangle to the terminal
    
    Args:
        char:
            The character to print
        
        height:
            The number of lines tall that the triangle should be
    
    Returns:
        None

    """
    dims = calc_dims(height)
    for reps in dims:
        print(char*reps)

# The only line of code not in a function is calling the function(s)
print_triangle(sys.argv[1], int(sys.argv[2]))
