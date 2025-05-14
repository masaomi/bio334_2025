
list1 = [1, 2, 3, 4, 5, 6]  # initialization of a list
total = 0                   # initialization of total variable
for i in list1:             # iteration of each element of the list
    total += i              # add the element to the total variable
print("total =", total)     # show the result

total = sum(list1)          # simple implementation
print("total = %d" % total) # show in a different way

total = sum(range(1, 7))    # simple implementation
print("total = %d" % total) # show in a different way

