
seq1 = "ATGC"                   # First sequence
seq2 = "ATAT"                   # Second sequence 

sequences = [seq1, seq2]        # Define a sequences list object having two sequences

for i in range(0, len(seq1)):   # Iteration with i that indicates the index of nucleotide position
    alleles = []                # Initialize alleles list in which allele data will be stored
    for seq in sequences:       # Check the two sequences with iteration
        alleles.append(seq[i])  # Each nucleotide at the same position is added in the alleles list
    #print alleles,              # python 2
    print(alleles, end="\t")   # python 3 
    if len(set(alleles)) > 1:   # Check the number of unique element in the alleles 
        print("segregated")     # in the case of more than two alleles are detected
    else:
        print("not segrated")   # in the case of only one kind of nucleotide is detected at the position
