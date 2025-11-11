print('x y z w') #переменные из условий
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((x <= y) and (y <= w)) or (z == (x or y))): #функция из условий
                    print(x, y, z, w)

# для всех заданий одно и тоже