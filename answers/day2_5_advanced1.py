

import sys
import glob # import glob module to use glob method
import os   # import os module to use system method
from module_gid_pi_td import gid_pi_td as gpd # import a custom module

print("GeneID\tpi\tTajimas_D")
#for file in glob.glob("HMA4_aligned_fasta_Alyr_origin/*.fasta"): # iterate all athal_chr*.fa files
for file in sorted(glob.glob(sys.argv[1] + "/*.fasta")): # iterate all athal_chr*.fa files
  print(gpd(file))
