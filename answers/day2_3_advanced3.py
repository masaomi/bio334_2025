import sys

def load_fasta(fasta):
    sequences = []
    with open(fasta) as f:
        for line in f:
            if not line.startswith(">"):
                sequences.append(line.rstrip())
    return sequences

def calc_maf(counts):
    if len(counts) == 1:  # Only one allele present
        return 0.0
    total = sum(counts.values())
    if total == 0:
        return 0
    maf = min(counts.values()) / total
    return maf

def calc_daf(counts, derived_allele):
    total = sum(counts.values())
    if total == 0 or derived_allele is None:
        return 0
    daf = counts.get(derived_allele, 0) / total
    return daf

def count_seg_sites(sequences, outgroup_seq):
    total_seg_sites = 0
    derived_allele_freqs = []

    for i in range(len(sequences[0])):
        ingroup_alleles = [seq[i] for seq in sequences]
        count = {}
        for allele in ingroup_alleles:
            if allele in count:
                count[allele] += 1
            else:
                count[allele] = 1
        
        # Determine the derived allele
        #derived_allele = None
        #if outgroup_seq[i] in count:
        #    if len(count) == 1:
        #        derived_allele = None
        #    else:
        #        derived_allele = min(count, key=lambda k: count[k] if k != outgroup_seq[i] else float('inf'))
        #else:
        #    derived_allele = outgroup_seq[i]

        derived_allele = None
        if outgroup_seq[i] in "ATGC":  # ignore Ns or gaps
            alleles = set(ingroup_alleles)
            if len(alleles) > 1 and outgroup_seq[i] in alleles:
                derived_candidates = alleles - {outgroup_seq[i]}
                if len(derived_candidates) == 1:
                    derived_allele = list(derived_candidates)[0]
                else:
                    # Multiple derived alleles → optional: skip or choose most frequent?
                    derived_allele = max(derived_candidates, key=lambda k: count.get(k, 0))


        # Calculate MAF and DAF
        maf = calc_maf(count)
        daf = calc_daf(count, derived_allele)
        
        if len(set(ingroup_alleles)) > 1:
            total_seg_sites += 1
            print(f"Position {i}: segregating, MAF={maf:.3f}, DAF={daf:.3f}, Derived Allele={derived_allele}")
        else:
            print(f"Position {i}: not segregating, MAF={maf:.3f}, DAF={daf:.3f}, Derived Allele={derived_allele}")

        derived_allele_freqs.append(daf)

    return total_seg_sites, derived_allele_freqs

if __name__ == "__main__":
    sequences = load_fasta(sys.argv[1])
    outgroup_seq = load_fasta(sys.argv[2])[0]  # Assume outgroup FASTA has a single sequence

    total_seg_sites, derived_allele_freqs = count_seg_sites(sequences, outgroup_seq)
    print("Total segregating sites =", total_seg_sites)
    print("Derived Allele Frequencies =", derived_allele_freqs)

