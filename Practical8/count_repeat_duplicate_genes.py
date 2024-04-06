def count_repeat_in_sequence(sequence, repeat):
    return sequence.count(repeat)

def write_fasta(genes, repeat, output_file):
    with open(output_file, 'w') as f:
        for gene_name, sequence in genes.items():
            repeat_count = count_repeat_in_sequence(sequence, repeat)
            fasta_header = f">{gene_name}_{repeat_count}"
            f.write(fasta_header + '\n')
            f.write(sequence + '\n')

def main():
    # Step 1: Ask the user for input
    repeat_choices = ['GTGTGT', 'GTCTGT']
    while True:
        user_input = input("Please enter one of the two repetitive sequences ('GTGTGT' or 'GTCTGT'): ")
        if user_input in repeat_choices:
            break
        print("Invalid input. Please try again.")

    # Create the output file name
    output_file = f"{user_input}_duplicate_genes.fa"

    # Step 2: Assume we have a dictionary of genes with their sequences (this would come from your genome data)
    # For the sake of this example, let's create a fake dataset
    genes = {
        'gene1': 'ATGTGTGTCTAGCTAGCTAG',
        'gene2': 'GTCTGTCTGTCTGTGTCTGT',
        'gene3': 'ACGTAGCTAGCT',
        'gene4': 'GTGTGTGTGTGTGT',
    }

    # Filter genes that contain the given repeat
    filtered_genes = {gene: seq for gene, seq in genes.items() if user_input in seq}

    # Step 3: Write the FASTA file
    write_fasta(filtered_genes, user_input, output_file)

    print(f"The FASTA file '{output_file}' has been created successfully!")

if __name__ == "__main__":
    main()
