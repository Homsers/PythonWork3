import random

mas=[]
a = 1
b = 0
for i in range(5): 
    mas.append(random.randint(0, 10)) 
print(mas)

result=[]
for i in range((len(mas)+1)//2):
    result.append(mas[i]*mas[len(mas)-1-i])
print(result)    
    



