
with open('37337.txt') as f:
    numb = list(map(int, f.readlines()))

count = 0
max_sum = 0

for i in range(len(numb)-1):
    a = numb[i]
    b = numb[i+1]
    if a%160 != b%160 and a%7==0 or b%7==0:
        count += 1
        if a + b > max_sum:
            max_sum = a+b

print(count)
print(max_sum)