import random
mas=[]
mas2 = []
a = 0
b = 0
for i in range(10): 
    mas.append(random.randint(1, 10)) 
print(sorted(mas))


[mas2.append(i) for i in mas if i not in mas2]
print(sorted(mas2))
