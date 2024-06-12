#!/usr/bin/env python3
import sys
import pandas as pd
blastpath = sys.argv[1]
bedpath = sys.argv[2]
outputpath = sys.argv[3]

blast = pd.read_csv(blastpath, sep='\t', header=None)
bed = pd.read_csv(bedpath, sep='\t', header=None)
identity_condition = blast.iloc[:, 2] > 30.0
length_condition = blast.iloc[:, 3] > 0.9 * blast.iloc[:, 12]
filtered = blast[identity_condition & length_condition]

uniques = set()
with open(outputpath, 'a') as file:
    for i in range(0,len(filtered)):
        blast_start = filtered.iloc[i,8]
        blast_end = filtered.iloc[i,9]
        blast_seqid = filtered.iloc[i,1]
        for j in range(0, len(bed)):
            bed_start = bed.iloc[j,1]
            bed_end = bed.iloc[j,2]
            bed_seqid = bed.iloc[j,0]
            gene_name = bed.iloc[j,3]
            if blast_seqid != bed_seqid:
                continue
            if blast_start > bed_start and blast_end < bed_end:
                if gene_name not in uniques:
                    file.write(gene_name + "\n")
                    uniques.add(gene_name)

with open(outputpath, 'r') as file:
    lines = file.readlines()
    count = len(lines)
print("The number of homologs is: " , count)