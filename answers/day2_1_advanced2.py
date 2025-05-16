
import sys      # import sys module to open and close methods

total_size = 0                 # Initialize a variable to store the genome size
gc_count = 0
file = open(sys.argv[1])        # Open a fastq file
line_count = 0
read_count = 0
for line in file:               # Read line by line using for statement
    if line_count % 4 == 1:      # Check the line beginning with '>', namely it checks if the line is the annotation or sequence
        total_size += len(line.rstrip())   # If the line is sequence data, the length of the nucleotide string will be added to the variable. 
        gc_count += line.count("G")    # Count the number of 'G' in the line
        gc_count += line.count("C")    # Count the number of 'C' in the line
        read_count += 1
    line_count += 1
file.close()                                # Close the file

print("Total reads =", read_count)  
print("Total size =", total_size, "bp") 
print("Average read length =", float(total_size)/read_count)
print("GC content = GC count/total size =", float(gc_count)/total_size) 

