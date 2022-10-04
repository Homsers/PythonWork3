import random
mas=[]
a = 0
for i in range(5): 
    mas.append(random.randint(0, 10)) 
print(mas)

for i in range(len(mas)):
    if i % 2 == 1:
        print(mas[i])
        a = a + mas[i]
print('=' f'{a}')