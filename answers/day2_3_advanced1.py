

import sys

def load_fasta(fasta):  
    sequences = []      

    f = open(fasta)     
    for line in f:      
        if not line[0] == ">":  
            sequences.append(line.rstrip()) 
    f.close()           
    return sequences    


def calc_pi(sequences):       
    total_diff = 0  
    for i in range(0, len(sequences)):                      
        for j in range(i+1, len(sequences)):                
            for k in range(0, len(sequences[i])):           
                if not sequences[i][k] == sequences[j][k]:  
                    total_diff += 1                         
    
    num_sequences = len(sequences)                          
    len_sequence = len(sequences[0])                        
    combination = num_sequences*(num_sequences-1)/2.0
    PI = total_diff/combination                             
    pi = total_diff/combination/len_sequence                
    return pi


sequences = load_fasta(sys.argv[1])
print("pi =", calc_pi(sequences))

def calc_heterozygosity(sequences):
    num_sequences = len(sequences)
    len_sequence = len(sequences[0])
    total_H = 0
    valid_sites = 0

    for i in range(len_sequence):
        freq = {}
        total = 0

        # Count nucleotides at position i (only A, T, G, C)
        for seq in sequences:
            base = seq[i]
            if base in "ATGC":
                if base not in freq:
                    freq[base] = 1
                else:
                    freq[base] += 1
                total += 1

        if total < 2:
            continue  # skip sites with fewer than 2 valid bases

        # Calculate ∑p_i^2
        p_squared_sum = 0
        for base in freq:
            p = freq[base] / total
            p_squared_sum += p * p

        # H_site = 1 - ∑p_i^2
        H_site = 1 - p_squared_sum
        total_H += H_site
        valid_sites += 1

    # Return average heterozygosity across all valid sites
    return total_H / valid_sites if valid_sites > 0 else 0

print("Heterozygosity (H) =", calc_heterozygosity(sequences))

def calc_theta(sequences):
    num_sequences = len(sequences)
    len_sequence = len(sequences[0])
    S = 0

    for i in range(len_sequence):
        bases = [seq[i] for seq in sequences]
        base_set = set(bases)
        if len(base_set) > 1:  # Polymorphic site
            S += 1

    a1 = sum(1.0 / i for i in range(1, num_sequences))
    theta = S / a1 / len_sequence
    return theta

print("Theta (θ) =", calc_theta(sequences))

