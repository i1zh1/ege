#ПРИМЕР

with open('17_example.txt') as f:
    numbers = list(map(int, f.readlines()))

count = 0
max_sum = -20000  # минимально возможная сумма двух чисел

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i+1]
    if a % 3 == 0 or b % 3 == 0:
        count += 1
        if a + b > max_sum:
            max_sum = a + b

print(count, max_sum)