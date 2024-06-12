#!/usr/bin/env python3

import sys

def newickCheck(input : str) -> str:
	""" checks if string adheres to Newick Format
		each node of a tree must be enclosed within parentheses 
		and there can not be a close parenthesis that does not 
		follow an open parenthesis
	
	args: 
		input: string possibly representing a Newick format tree
		
	returns: 
		message that states "PAIRED" or "NOT PAIRED"
	"""
	
	ls = []
	
	for char in input: 
		if char == '(': 
			ls.append(char)
		elif char == ')': 
			if len(ls) == 0 or ls.pop() != '(': 
				return "NOT PAIRED"
			
	return "PAIRED" if not ls else "NOT PAIRED"
	
# the only line of code not in a function is calling a function
message = newickCheck(sys.argv[1])
print(message)
