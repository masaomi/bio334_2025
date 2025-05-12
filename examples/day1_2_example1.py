

list1 = [1, 2, 3, 4, 5, 6]  # First list
list2 = [1, 2, 0, 4, 5, 0]  # Second list

for i in range(0, len(list1)):  # Iteration with the index of list1
    print("%s %s : " % (list1[i], list2[i]), end = "") #python3
    #print "%s %s : " % (list1[i], list2[i]), #python2 
    if list1[i] == list2[i]:    # Comparison between each element of the same position
        print("True")           # In case of the two elements are same
    else:
        print("False")          # In case of the two elements are different

print("")
print("Another implementation")
for i in range(0, len(list1)):  # Iteration with the index of list1
    print("%s %s : " % (list1[i], list2[i]), end = "") #python3
    #print "%s %s : " % (list1[i], list2[i]), #python2
    print(list1[i] == list2[i]) # Show the comparison result

