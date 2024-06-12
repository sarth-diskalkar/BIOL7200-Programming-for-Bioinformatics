#!/usr/bin/env python3

# Usage q3_solution <blastfile> <bedfile> <assembly>
import sys

def read_blast_file(file: str) -> list[tuple[str, int, int]]:
    """Opens and reads file with blast results"""
    hits = []
    with open(file) as fin:
        for line in fin: # .readlines() is the default iter method for the open file class
            
            # unpack and convert types of desired columns. This is ugly. We'll revisit later...
            _, sid, pcnt, matchlen, _, _, _, _, sstart, send, _, _, qlen = line.split()
            pcnt = float(pcnt)
            matchlen = int(matchlen)
            sstart = int(sstart)
            send = int(send)
            qlen = int(qlen)
        
            # Keep hits that could be homologs
            if pcnt > 30 and matchlen > 0.9*qlen:
                # We could store matches as a list or tuple.
                # We won't want to modify the elements so a tuple is "safer" in that we then can't modify it by mistake
                hits.append((sid, sstart, send))
    return hits

def read_bed_file(file: str) -> list[tuple[str, int, int, str, str]]:
    feats = []
    with open(file) as fin:
        for line in fin:
            bed_sid, bed_start, bed_end, gene, _, strand = line.split() # an asterisk before a variable name when unpacking makes that variable store remaining elements
            bed_start = int(bed_start)
            bed_end = int(bed_end)
            
            feats.append((bed_sid, bed_start, bed_end, gene, strand))
    
    return feats

def find_homologs(
    blast_hits: list[tuple[str, int, int]],
    bed_feats: list[tuple[str, int, int, str, str]]
) -> list[tuple[str, int, int, str, str]]:
    homologs = []
    for blast_sid, blast_sstart, blast_send in blast_hits: # unpack our blast data
        for bed_sid, bed_start, bed_end, gene, strand in bed_feats:
            # Don't bother checking the rest if the sid doens't match
            if blast_sid != bed_sid:
                continue
            
            # Once we are dealing with features at higher index locations than our hit, go to the next hit (break loop over feats)
            if blast_sstart <= bed_start or blast_send <= bed_start:
                break
            
            # Otherwise, check if the hit is inside the feature
            if (blast_sstart > bed_start
                and blast_sstart <= bed_end
                and blast_send > bed_start
                and blast_send <= bed_end
            ):
                homologs.append((bed_sid, bed_start, bed_end, gene, strand))
                break # Each BLAST hit will only be in one feature so move to next hit once you've found it
    return homologs

def read_fasta(fasta_file: str) -> dict[str, str]:
    fasta_dict = {}
    with open(fasta_file) as fin:
        seq_lines = []
        for line in fin:
            if line[0] == ">":
                if seq_lines:
                    fasta_dict[header] = "".join(seq_lines)
                    seq_lines = []
                header = line.split()[0][1:] # word after ">"
                continue

            seq_lines.append(line.strip())
        fasta_dict[header] = "".join(seq_lines)
    return fasta_dict

def rev_comp(seq: str) -> str:
    revs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    rev_bases = [revs[base.upper()] for base in seq[::-1]]
    rev_seq = "".join(rev_bases)
    return rev_seq

def write_homologs(
    homologs: list[tuple[str, int, int, str, str]],
    fasta_dict: dict[str, str],
    outfile: str
) -> None:
    outcontents = []
    for bed_sid, bed_start, bed_end, gene, strand in homologs:
        if strand == "+":
            seq = fasta_dict[bed_sid][bed_start-1:bed_end]
        else:
            seq = rev_comp(fasta_dict[bed_sid][bed_start-1:bed_end])
        outcontents += [f">{gene}", seq]
    
    with open(outfile, 'w') as fout:
        fout.write("\n".join(outcontents) + "\n")


blastfile = sys.argv[1]
bedfile = sys.argv[2]
assembly = sys.argv[3]
outfile = sys.argv[4]

hits = read_blast_file(blastfile)
feats = read_bed_file(bedfile)
homologs = find_homologs(hits, feats)
fasta_dict = read_fasta(assembly)

# Get the unique homologs using a set()
unique_homologs = set(homologs)

write_homologs(unique_homologs, fasta_dict, outfile)
