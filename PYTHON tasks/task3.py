import random
mas=[]
for i in range(5): 
    mas.append(round(random.uniform(1,5), 2))
print(mas)

min = 1
max = 0
for i in mas:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i) 
print(round(max, 2))
print(round(min, 2))
print('разница равна')
print(round(max-min, 2))