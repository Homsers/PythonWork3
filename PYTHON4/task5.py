import json


def save():
    with open("mp3_Bot.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(arr, ensure_ascii=False))
    print("mp3 player сохранен в файле мр3_Вот")


from random import *
from traceback import print_list
from pprint import pprint
Rock=['Rock']
Pop = ['Pop']
Rap = ['Rap']
Other = ['Other']
arr = [[Rock],[Pop],[Rap],[Other]]
arr2 = ['Rock', 'Pop', 'Rap', 'Other']

print(arr)

while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Бот-плеер начал свою работу ")
    elif command == "/stop":
        save()
        print("Бот остановил свою работу ")
        break
    elif command =="/all":
        print("Список музыки: ")
        print(arr)
    elif command == "/add rock":
            s = input("Название")
            Rock.append(s)
            print('успешно')
    elif command == "/add pop":
            s = input("Название")
            Pop.append(s)
            print('успешно')
    elif command == "/add rap":
            s = input("Название")
            Rap.append(s)
            print('успешно')
    elif command == "/add other":
            s = input("Название")
            Other.append(s)
            print('успешно')
    elif command == "/del rock":
            s = input("Название")
            Rock.remove(s)
            print('успешно')
    elif command == "/del pop":
            s = input("Название")
            Pop.remove(s)
            print('успешно')
    elif command == "/del rap":
            s = input("Название")
            Rap.remove(s)
            print('успешно')
    elif command == "/del other":
            s = input("Название")
            Other.remove(s)
            print('успешно')
    elif command == "/random":
        rnd = randint(0, len(arr2)-1)
        print("Случайный жанр - " + arr2[rnd])
    elif command == "/help":print("манул") 
    elif command == "/save":
        save()
    elif command == "/load":
        with open("mp3_Bot.json", "r", encoding="utf-8") as fh:
            arr=json.load(fh)
    else:
        print("Неопознанная команда.Просьба вызвать манула через /help!")
    


    
