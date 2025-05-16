
snps1 = {1: 'A', 3: 'G', 4: 'C'}
snps2 = {1: 'A', 4: 'T'}

print("Sample1: ", snps1)
print("Sample2: ", snps2)
pos1 = set(snps1.keys())
pos2 = set(snps2.keys())
common_pos = pos1 & pos2
exclor_pos = pos1 ^ pos2

diff = len(exclor_pos)
for pos in common_pos:
    if not snps1[pos] == snps2[pos]:
        diff += 1

print("The number of segregating sites = ", diff)

