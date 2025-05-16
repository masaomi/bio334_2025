

import sys
import glob # import glob module to use glob method
import os   # import os module to use system method

print("GeneID\tpi\tTajimas_D", flush=True)
#for file in glob.glob("HMA4_aligned_fasta_Alyr_origin/*.fasta"): # iterate all athal_chr*.fa files
for file in sorted(glob.glob(sys.argv[1] + "/*.fasta")): # iterate all athal_chr*.fa files
  command = "python3 gid_pi_td.py " + file # make a command
  #print(command)
  os.system(command)    # execute the command
