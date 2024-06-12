#!/usr/bin/env python3

import sys

def build_base(char: str, height: int) -> None:
	"""Prints a triangle of text to the console
	
	Args:
		char: the character to print
		height: the number of characters tall the triangle should be

	Returns:
		None because there are no return statements in the function
		Prints text string to console as output
	"""
	empty= []
	if height % 2 == 0:
		for i in range(0,height//2):
			empty.append(char)
			print("".join(empty))
		print("".join(empty))    
		for i in range((height//2)-1,0,-1):
			del empty[i]
			print("".join(empty))
	if height % 2 == 1:
		for i in range(0,(height//2)):
			empty.append(char)
			print("".join(empty))
		empty.append(char)
		print("".join(empty))
		for i in range((height//2),0,-1):
			del empty[i]
			print("".join(empty))

build_base(str(sys.argv[1]),int(sys.argv[2]))