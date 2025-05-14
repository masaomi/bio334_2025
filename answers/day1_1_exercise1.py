lst = [1, 2, 3, 4, 5, 6]
total = 0
count = 0
for i in lst:
    total += i
    count += 1
print("list = ", lst)
print("mean = ", total / count)
print("mean = %.3f" % (total / count))
#print("mean = %f" % (sum(lst) / len(lst)))
