s = str(input())
t = int(input())
n = int(input())

x = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

y = {}
for z, w in x.items():
    for i, ch in enumerate(w, 1):
        y[ch] = (z, i)

tot = 0
prev = 0

for ch in s:
    d, k = y[ch]
    if d == prev:
        tot += min(t + k * n, 2 * n + k * n)
    else:
        tot += k * n
        prev = d

print(tot)




