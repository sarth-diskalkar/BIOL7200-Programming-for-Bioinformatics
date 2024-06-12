#!/bin/bash

query_seqs=$1
genome_assembly=$2
outfile=$3

# tblastn blasts protein queries against translated nucleotide subject
# \ can escape newlines so you can put each input on a different line
# for improved readability
# Can't comment individual lines though as \ essentially makes the whole thing 
# a single line


tblastn \
	-query $query_seqs \
	-subject $genome_assembly \
	-outfmt '6 std qlen' \
	-task tblastn-fast \
| awk '$3>30 && $4>0.9*$13' > $outfile
	
echo "$(wc -l $outfile | cut -d' ' -f1) matches found in $genome_assembly"


# Some people used -task tblastn or tblastn-fast.
# tblastn is default so setting it changes nothing
# see `tblastn -help | grep -EA 2 "^\s+-task"`
# tblastn-fast is faster, but uses a longer word size in the search
# try both by running the command in your terminal and assess the differences
# also try running the exercise4 script with or without tblastn-fast
# does it make a difference to the overall output? Why/why not?
# We can discuss this in class when talking about the ex4 script
