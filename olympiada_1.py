a = int(input())
b = int(input())

c = (a + 3) // 4

z = b + 2 * (c - 1)
x = b + 2 * c

for i in range(z, x):
    if i % 6 == 0:
        print(i // 6)