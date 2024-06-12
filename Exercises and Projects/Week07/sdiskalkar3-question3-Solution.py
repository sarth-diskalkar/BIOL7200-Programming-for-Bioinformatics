#!/usr/bin/env python3
import sys

blastfile = sys.argv[1]
bedfile = sys.argv[2]
assembly_file = sys.argv[3]
output_file = sys.argv[4]

def reverse_complement(seq: str) -> str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

fasta_sequence = ""

with open(assembly_file, 'r') as f:
    for line in f:
        if not line.startswith(">"):
            fasta_sequence += line.strip()

print(fasta_sequence)

hits = []
with open(blastfile) as fin:
    for line in fin: 
        _, sid, pcnt, matchlen, _, _, _, _, sstart, send, _, _, qlen = line.split()
        pcnt = float(pcnt)
        matchlen = int(matchlen)
        sstart = int(sstart)
        send = int(send)
        qlen = int(qlen)
        if pcnt > 30 and matchlen > 0.9 * qlen:
            hits.append((sid, sstart, send))

feats = []
with open(bedfile) as fin:
    for line in fin:
        bed_sid, bed_start, bed_end, gene, strand, *_ = line.split()
        bed_start = int(bed_start)
        bed_end = int(bed_end)

        feats.append((bed_sid, bed_start, bed_end, gene, strand))

homolog_sequences = {}
for blast_sid, blast_sstart, blast_send in hits:
    for bed_sid, bed_start, bed_end, gene, strand in feats:
        if blast_sid != bed_sid:
            continue
        if blast_sstart <= bed_start or blast_send <= bed_start:
            break
        if (blast_sstart > bed_start and blast_sstart <= bed_end and
            blast_send > bed_start and blast_send <= bed_end):
            sequence = fasta_sequence[bed_start - 1: bed_end]
            if strand == "-":
                sequence = reverse_complement(sequence)
            if gene in homolog_sequences:
                homolog_sequences[gene].append(sequence)
            else:
                homolog_sequences[gene] = [sequence]
            break

with open(output_file, 'w') as out_content:
    for gene, sequences in homolog_sequences.items():
        sequence = "".join(sequences)
        out_content.write(f">{gene}\n{sequence}\n")

print(len(homolog_sequences))

