a = list(map(int, bin(int(input()))[2:]))
b=0
for i in a: 
    b+=i
a.append(b%2)
    
b=0
for i in a:
    b+=i
a.append(b%2)

print(int(''.join(map(str, a)), 2))
# ответ 102 подбором, решение заняло 9 минут(плохо, надо решать еще)

#НЕ всегда РАЦИОНАЛЬНО, ДЕЛАЙ ЧЕРЕЗ ЕКСЕЛЬ когда это можно