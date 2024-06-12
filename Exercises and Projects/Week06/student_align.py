#!/usr/bin/env python3

# extract seq1 and seq2
# remove white space (/n) at the end of seq 1 and seq2

import sys 

x = open(sys.argv[1], 'r')
sequences = x.readlines()
seq1 = sequences[1]
seq1_strip = seq1.strip() 
seq2 = sequences[3]
seq2_strip = seq2.strip()

# create loop to find corresponding symbols with the sequences
# convert string to numbers 

def matched_symbols(seq1, seq2):
    seq_length = min(len(seq1), len(seq2))

    for i in range(seq_length):
        if seq1[i] == seq2[i]:
            print('|', end='')
        else:
            print(' ', end='')
    print("") 

print(seq1_strip)
matched_symbols(seq1_strip, seq2_strip)
print(seq2_strip)
