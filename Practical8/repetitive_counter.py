import re

# Defines a sequence that contains repeating elements
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Define patterns for repeating elements, where regular expressions are used to match overlapping GTGTGT and GTCTGT
pattern = re.compile(r'GT(G|C)TGT')

# Find all matches
matches = pattern.findall(seq)

# Calculate the number of matches
count = len(matches)

# Print and result
print(f"Total number of overlapping repeat elements: {count}")

