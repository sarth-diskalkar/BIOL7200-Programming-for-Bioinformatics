import sys

blast_output = sys.argv[1]
bed_file = sys.argv[2]
out_file = sys.argv[3]

perc_identity = 30
perc_length = 0.9

unique_gene_names = ""

with open(blast_output, "r") as blast_hits:
    for line in blast_hits:
        fields = line.strip().split('\t')
        if float(fields[2]) > perc_identity and float(fields[3]) >= float(fields[12])*perc_length:
            blast_seqid, blast_start, blast_stop = fields[1], int(fields[8]), int(fields[9])
        else:
            continue
        with open(bed_file, "r") as bed_features:
            for bed_line in bed_features:
                bed_fields = bed_line.strip().split('\t')
                bed_seqid, bed_start, bed_stop, bed_gn = bed_fields[0], int(bed_fields[1]), int(bed_fields[2]), bed_fields[3]
                
                #Don't check if we're on the wrong contig
                if blast_seqid != bed_seqid:
                    continue

                #Don't check stop if we haven't reached hit location yet
                if blast_start > bed_stop:
                    continue

                #Don't check remaining features if we're past the hit location
                if blast_start < bed_start:
                    break

                #Check if the coordinates overlap
                if blast_start > bed_start and blast_start < bed_stop and blast_stop > bed_start and blast_stop < bed_stop and bed_gn not in unique_gene_names:
                    unique_gene_names += bed_gn + "\n"

with open(out_file, "w") as output:
    output.write(unique_gene_names)

print("Number of homolog matches in", bed_file + ":", unique_gene_names.count('\n'))