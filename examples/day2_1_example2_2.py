
import sys                      # Import sys module to use open method
with open("input.fa") as file:  # Open the file input.fa and return the file handle
    for line in file:           # Repeat reading line by line from the file
        print(line.rstrip())    # Show the line with the line break removed

