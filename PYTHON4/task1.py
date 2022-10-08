number1 = int(input("Введите число: "))
i = 2 
mas = []
while i <= number1:
    if number1 % i == 0:
        mas.append(i)
        number1 //= i
        i = 2
    else:
        i += 1
print(mas)