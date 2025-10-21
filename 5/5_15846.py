inp = int(input())
a = list(map(int, bin(inp)[2:]))
b=0
if inp % 2 == 0:
    a += [0, 0]
elif inp % 2 != 0:
    a += [1, 1]
print(int(''.join(map(str, a)), 2))
#119 подбором, за 5 минут. ответ 29 в этом случае