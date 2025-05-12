
lst = ["a", "b", "c", "d", "e"]    # Initialization of list

# Permutation list
print("permutations")
for i in range(0, len(lst)):       # Iteration of list with index, i becomes the first list index
    for j in range(0, len(lst)):   # inside loop of iteration, j becomes the second list index
        if not lst[i] == lst[j]:  # except for the selected elements are same
            print(lst[i], lst[j]) # show each element of two lists

# Combination list
print("")
print("combinations")
for i in range(0, len(lst)):       # First loop
    for j in range(i+1, len(lst)): # Second loop, be careful of the start index
        print(lst[i], lst[j])     # show each element of two lists
