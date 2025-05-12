
# List of Lists

lst1 = [0, 1]
lst2 = [2, 3]

lst = [lst1, lst2]
print(lst[0][0]) # => 0
print(lst[0][1]) # => 1
print(lst[1][0]) # => 2
print(lst[1][1]) # => 3
print("")

# List of Strings

str1 = "AT"
str2 = "GC"

lst = [str1, str2]
print(lst[0][0]) # => A
print(lst[0][1]) # => T
print(lst[1][0]) # => G
print(lst[1][1]) # => C
print("")

for i in range(0, 2):     # select string
    for j in range(0, 2): # select position
        print(lst[i][j])


