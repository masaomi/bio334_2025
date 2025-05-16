
import glob

samples = []
for file_name in glob.glob("*.vcf"):
    f = open(file_name)
    snps = {}
    for line in f:
        pos = line.split()[2]
        nuc = line.split()[4]
        snps[pos] = nuc
    f.close()
    samples.append(snps)

print(samples)

