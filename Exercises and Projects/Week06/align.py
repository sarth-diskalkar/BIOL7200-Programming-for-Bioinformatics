#!/usr/bin/env python3

seqs_dict = {}
with open("aligned.fna") as fin:
	this_seq = []
	for line in fin:
		if line[0] == ">":
			if this_seq: # False if empty
				seqs_dict[header] = "".join(this_seq) # list -> str
			header = line.strip()[1:] # excluding ">""
			this_seq = []
		else:
			this_seq.append(line.strip())
	# Once loop ends, add final sequence to dict
	seqs_dict[header] = "".join(this_seq) 

aligned = []
for a,b in zip(seqs_dict["Pa"], seqs_dict["Vc"]):
	if a == b:
		aligned.append("|")
	else:
		aligned.append(" ")
aligned = "".join(aligned)

print(seqs_dict["Pa"])
print(aligned)
print(seqs_dict["Vc"])

