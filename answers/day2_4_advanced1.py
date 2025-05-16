import sys
import math

# Load FASTA file and extract sequences
def load_fasta(fasta):
    sequences = []
    with open(fasta) as f:
        for line in f:
            if not line.startswith(">"):
                sequences.append(line.strip())
    return sequences

# Count nucleotide differences between two sequences
def count_diff(seq1, seq2):
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

# Compute total pairwise differences for π (nucleotide diversity)
def count_total_diff(sequences):
    total_diff = 0
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            total_diff += count_diff(sequences[i], sequences[j])
    return total_diff

# Count the number of segregating sites (S)
def count_seg_sites(sequences):
    total_seg_sites = 0
    for i in range(len(sequences[0])):
        site = [seq[i] for seq in sequences]
        if len(set(site)) > 1:
            total_seg_sites += 1
    return total_seg_sites

# Compute nucleotide diversity (π)
def nucleotide_diversity(sequences):
    n = len(sequences)
    L = len(sequences[0])
    total_diff = count_total_diff(sequences)
    pi = total_diff / (n * (n - 1) / 2) / L
    return pi

# Compute classical constants used in Tajima's D and other neutrality tests
# Based on: Tajima (1989), Fay & Wu (2000), Zeng et al. (2006)
def compute_constants(n):
    a1 = sum(1.0 / i for i in range(1, n))
    a2 = sum(1.0 / (i ** 2) for i in range(1, n))
    b1 = (n + 1) / (3 * (n - 1))
    b2 = (2 * (n ** 2 + n + 3)) / (9 * n * (n - 1))
    c1 = b1 - 1 / a1
    c2 = b2 - ((n + 2) / (a1 * n)) + (a2 / (a1 ** 2))
    e1 = c1 / a1
    e2 = c2 / (a1 ** 2 + a2)
    return a1, a2, e1, e2

# Fay and Wu’s H statistic and Z-score normalization
# References:
# - Fay & Wu (2000), Genetics 155(3):1405–1413
# - Zeng et al. (2006), Genetics 174(3):1071–1079
def fay_wu_h_z(sequences, outgroup_seq):
    n = len(sequences)
    L = len(sequences[0])

    pi = nucleotide_diversity(sequences)

    theta_H_sum = 0
    S = 0  # Number of informative segregating sites with valid ancestral state

    for i in range(L):
        ancestral = outgroup_seq[i]
        site_bases = [seq[i] for seq in sequences if seq[i] in "ATGC"]

        if len(set(site_bases)) < 2:
            continue

        derived_count = sum(1 for base in site_bases if base != ancestral)
        if derived_count == 0:
            continue

        theta_H_sum += 2 * derived_count ** 2
        S += 1

    if S == 0:
        return 0.0, 0.0

    theta_H = theta_H_sum / (n * (n - 1) * S)
    H = pi - theta_H

    # Approximate variance of H based on literature (Zeng et al. 2006)
    a1, a2, _, _ = compute_constants(n)
    theta = S / a1  # Watterson's estimator of theta

    var_H = theta * ((2 * (n ** 2 + n + 3)) / (9 * n * (n - 1)) -
                     (a1 * (n + 2)) / (n * (n - 1)) +
                     (a2 / (a1 ** 2)))

    if var_H <= 0:
        return H, 0.0

    z_H = H / math.sqrt(var_H)
    return H, z_H

# Tajima's D implementation (standardized)
# Reference: Tajima (1989), Genetics 123(3):585–595
def tajimas_d(sequences):
    n = len(sequences)
    L = len(sequences[0])
    pi = nucleotide_diversity(sequences)
    S = count_seg_sites(sequences)

    a1, a2, e1, e2 = compute_constants(n)
    theta = S / a1  # Watterson's theta
    var_d = e1 * S + e2 * S * (S - 1)

    if var_d <= 0:
        return 0.0

    D = (pi - theta / L) / math.sqrt(var_d / L**2)
    return D

# Main execution
if __name__ == "__main__":
    sequences = load_fasta(sys.argv[1])
    outgroup_sequence = load_fasta(sys.argv[2])[0]

    print("Tajima's D =", tajimas_d(sequences))
    H, ZH = fay_wu_h_z(sequences, outgroup_sequence)
    print("Fay and Wu's H =", H)
    print("Z(H) =", ZH)

