def count_overlapping_repeats(seq, repeats):
    count = 0
    for i in range(len(seq) - len(repeats[0]) + 1):  # Iterate from the first character to the last possible complete match
        for pattern in repeats:  # Check each repeating pattern
            if seq[i:i+len(pattern)] == pattern:  
                count += 1  
    return count

# Define sequences and repeat patterns
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
repeats = ['GTGTGT', 'GTCTGT']

# Call the function and print the result
total_repeats = count_overlapping_repeats(seq, repeats)
print(f"Total number of overlapping repeat elements: {total_repeats}")


