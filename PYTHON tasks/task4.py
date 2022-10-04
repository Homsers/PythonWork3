a = ""

n = int(input('Введите число '))
while n != 0:
    a = str(n%2) + a
    n //=2
print(a)