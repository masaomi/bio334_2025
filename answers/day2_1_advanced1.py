
import sys      # import sys module to open and close methods

genome_size = 0                 # Initialize a variable to store the genome size
gc_count = 0
file = open(sys.argv[1])        # Open a fasta file, athal_genome.fa
for line in file:               # Read line by line using for statement
    if not line[0] == ">":      # Check the line beginning with '>', namely it checks if the line is the annotation or sequence
        genome_size += len(line.rstrip())   # If the line is sequence data, the length of the nucleotide string will be added to the variable. 
        for s in line:                      # Check each character of the line
            if s == 'G' or s == 'C':        # Check the character is 'G' or 'C'
                gc_count += 1               # Count up the gc_count variable
file.close()                                # Close the file

print("Genome size =", genome_size, "bp")   # Show the genome_size
print("GC content = GC count/genome size =", float(gc_count)/genome_size) # GC content

