
import sys                  # Import sys module

def load_fasta(fasta):      # Define load_fasta method, fasta is an argument data file
    sequences = []          # Initialize seuqnces list

    f = open(fasta)         # Open a fasta file
    for line in f:          # Read line by line from the fasta file
        if not line[0] == ">": # Skip annotation lines
            sequences.append(line.rstrip()) # keep sequence data in sequences list
    f.close()               # Close the file 
    return sequences        # Return the sequences list

def calc_maf(dict):
    total = sum(dict.values())
    maf = 10
    for key,value in dict.items():
        m = value/total
        maf = min(m, maf)
    return maf

def count_seg_sites(sequences):             # Define a method to count total number of segregating sites from sequences list object
    total_seg_sites = 0                     # Initialize a variable to keep the total number ofsegregating sites
    for i in range(0, len(sequences[0])):   # Iteration of selecting a postion
        alleles = []                        # Initialize a list object to keep alleles data at the postion
        count = {}
        for seq in sequences:               # Itelation of selecting a sequence
            alleles.append(seq[i])          # Keep the nucleotide in alleles list
            if seq[i] in count:
                count[seq[i]] += 1
            else:
                count[seq[i]] = 1

        print(sorted(set(alleles)), end="\t")   # python3  
        if len(set(alleles)) > 1:           # Check if it is segregating sites or not
            print("segregating, MAF=", calc_maf(count))
            total_seg_sites += 1            # If it is segregating, count up the variable
        else:
            print("not segregating")

    return total_seg_sites                  # Return the total number of segregaed sites

sequences = load_fasta(sys.argv[1])                 # Call load_fasta method with a fasta file path and load sequence data
total_seg_sites = count_seg_sites(sequences)        # Calculate the total number of segregating sites
print("Total segregating sites =", total_seg_sites)  # Show the result

