import re

# Open the input FASTA file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile:
    # Initialize a list to store the sequences and descriptions of the genes containing 'duplication'
    duplicate_genes = []
    current_gene = None
    current_seq = []
    
    for line in infile:
        # If the line begins with '>', a new sequence begins
        if line.startswith('>'):
            # Extract gene names and descriptions
            header = line.strip()
            gene_name, description = header[1:].split(' ', 1)
            
            # Check whether the description contains 'duplication'
            if 'duplication' in description:
                # If the current gene contains duplication, the current gene sequence and description are saved
                if current_gene:
                    duplicate_genes.append((current_gene, ''.join(current_seq)))
                
                # Start a new gene sequence
                current_gene = gene_name
                current_seq = [line.strip()[1:]]  
            # If the gene is not new or does not contain 'duplication' in the description, the sequence of the current gene will continue to be collected
            else:
                if current_gene:
                    current_seq.append(line.strip())
        # If the line does not start with '>', it is part of a sequence
        else:
            if current_gene:
                current_seq.append(line.strip())
    
    # Save the sequence of the last gene
    if current_gene:
        duplicate_genes.append((current_gene, ''.join(current_seq)))

# Open the output FASTA file
with open('duplicate_genes.fa', 'w') as outfile:
    # Iterate through the list of genes containing 'duplication' and write to the file
    for gene_name, sequence in duplicate_genes:
        outfile.write(f'>{gene_name}\n')
       
        for i in range(0, len(sequence), 80):
            outfile.write(sequence[i:i+80] + '\n')

print("Finished extracting duplicate genes and writing to duplicate_genes.fa")
