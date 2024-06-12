#!/bin/bash

query_file="$1"
subject_file="$2"
bedfile="$3"
outfile="$4"

tblastn \
    -query "$query_file" \
    -subject "$subject_file" \
    -outfmt '6 std qlen' \
    -task tblastn \
| gawk '$3>30 && $4>0.9*$13' > "$outfile.tmp"

echo "$(wc -l "$outfile.tmp" | cut -d' ' -f1) matches found in $subject_file"
gene_file=$(mktemp)

while read -r _ a b c; do
    gawk -v start="$b" -v end="$c" '$2 >= start && $3 <= end {print $4}' "$outfile.tmp" >> "$gene_file"
done < "$bedfile"

sort -u "$gene_file" > "$outfile"

rm -f "$gene_file"

echo "Gene names containing predicted HK domains have been written to $4"

