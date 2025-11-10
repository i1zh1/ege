a = list(map(int, bin(int(input()))[2:]))
print(a)
summ = 0
for i in a:
    summ += i
a.append(summ%2)
    
print(a)
summ = 0
for i in a:
    summ+=i
a.append(summ%2)

print(a)
print(int(''.join(map(str, a)), 2))

#НЕ РАЦИОНАЛЬНО, ДЕЛАЙ ЧЕРЕЗ ЕКСЕЛЬ