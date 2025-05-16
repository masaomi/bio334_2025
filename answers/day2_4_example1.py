
x = 0
n = 10
for i in range(1, n):
    x += 1.0/i

# Another way
a = [1.0/i for i in range(1, n)]
y = sum(a)

print(x)
print(sum(a))
