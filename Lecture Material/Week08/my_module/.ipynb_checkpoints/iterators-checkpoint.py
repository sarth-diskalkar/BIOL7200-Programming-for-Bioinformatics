def iter_int(num: int) -> int:
	snum = str(num)
	power = len(snum)
	for n in snum:
		n = int(n)
		n = n * 10**(power-1)
		yield n
		power -=1
