
import sys                  # Import sys module to use open method
file = open(sys.argv[1])    # Open the file and return the file handle
for line in file:           # Repeat reading line by line from the file
    print(line.rstrip())    # Show the line with the line break removed
file.close()                # Close the file

