
import os           # Import os module to call Unix command in a Python script
#import commands    # Only Python 2
import subprocess   # Call Unix comamnd and return the result

os.system("pwd")    # Run pwd command, and the result is shown in a stardard output

#result = commands.getoutput("pwd")  # Python 2
result = subprocess.getoutput("pwd") # Only Python 3, Run pwd and return the result
print(result)

