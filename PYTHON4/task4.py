a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

def nok(a,b):
    i = min(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            break
        i += 1
    print(i)
nok(a, b)
