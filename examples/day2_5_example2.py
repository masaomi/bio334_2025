
import glob # import glob module to use glob method
import os   # import os module to use system method

for file in glob.glob("athal_chr*.fa"): # iterate all athal_chr*.fa files
  command = "python3 day2_1_exercise1.py " + file # make a job command
  print(command)                        # show the command
  os.system(command)                    # execute the command
