import sys
import statistics
import random
import csv
import re


#
# Classes
#


# # Class - це як шаблон, а об'єкт — це конкретний екземпляр цього креслення
# class Hi:
#     # __init__ - задає, що відбувається при створенні об'єкта
#     # self - об'єкт на який діє клас
#     # name і age - це параметри які вводяться
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # Це функція яку може виконувати class
#     def Hello(self):
#         print(f"{self.name} say: Hi!")
#
# my_Hi = Hi("Andriy", 13)
#
# print(my_Hi.name)
# print(my_Hi.age)
# my_Hi.Hello()





#
# file
#


# name = input("Write your name - ")
# clas = input("Write your class - ")
# with open("test.csv", "a") as file:
#     # .writer - в бібліотеці csv записує інформацію в файл
#     # writer = csv.writer(file)
#     # fieldnames - вказує назву колони
#     writer = csv.DictWriter(file, fieldnames=["name", "clas"])
#     # .writerow - використовується для запису одного рядка в CSV-файл.
#     writer.writerow({"name": name, "clas":clas})

# humans = []
# with open("test.csv") as file:
#     # .reader - читає CSV-файл пострічково і перетворює кожен рядок на список значень
#     # reader = csv.reader(file)
#     # for name, clas in reader:
#     #     humans.append({"name" : name,"clas" : clas})
#     # .DictReader - читає CSV-файл і автоматично перетворює кожен рядок у словник
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Обов'язково аби в .csv файлі не було відступів у назвах
#         humans.append({"name": row["name"], "clas": row["clas"]})
#
# for human in sorted(humans, key=lambda x: x["name"]):
#      print(f"{human["name"]}, {human["clas"]}")

# # lambda - це функція яка обмежується одним вираженням її можна запхати в змінну
# square = lambda x: pow(x, 2)
# print(square(2))

# # Приклад з використанням словника
# humans = []
# with open("test.csv") as file:
#     for line in file:
#         name, clas = line.rstrip().split(",")
#         human = {"name" : name, "clas" : clas}
#         humans.append(human)
#
# def get_name(x):
#     return x["name"]
#
# # key - сортує словники за тим значеням яка задане
# for human in sorted(humans, key=get_name):
#     print(f"{human["name"]}, {human["clas"]}")

# # Приклад з використанням масива та сортування
# names = []
# with open("test.csv") as file:
#     for line in file:
#         name, clas = line.rstrip().split(",")
#         names.append(f"{name}, {clas}")
#
# for i in sorted(names):
#     print(i)

# # .csv - розширення для файлів таблиць
# with open("test.csv") as file:
#     for line in file:
#         # При введені двох зміних з методом .split() вони значитимуть
#         # перший ше що до видаленого елемента строки а другий після
#         name, clas = line.rstrip().split(",")
#         print(f"{name}, {clas}")

# # Приклад з використанням sorted()
# names = []
# with open("test.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# # reverse=True - сортує в зворотньому порядку
# for name in sorted(names, reverse=True):
#     print(f"hello, {name}")

# # with - автоматично закриває файл після виконання певних вказаних дій
# # r - означає що данні читаються з файла
# with open("test.txt", "r") as file:
#     # Метод .readlines() - зчитує всі рядки з файлу та повертає їх у вигляді списку рядків.
#     # lines = file.readlines()
#     for line in file:
#         print(f"hello, {line.rstrip()}")

# for line in lines:
#     #  видаляє завершальні символи з рядка
#     print(f"hello, {line.rstrip()}")
# # open() - відкриває певний файл та робить вказані дії
# name = input("What your name - ")
# # w -означає що в файл очищяється і записується данні
# # file = open("test.txt", "w")
# # a -означає що в кінець файла додається якась інформація
# file = open("test.txt", "a")
# # .write - записує в файл пефну інформацію
# file.write(f"{name}\n")
# # .close - закриває файл перестає його зчитувати
# file.close()




#
# bace libraries
#


# # regex - бібліотека яка використовується для пошуку або перевірки
# # import re

# # csv - базова бібліотека яка розволяє зчитувати .csv файли (таблиці)
# # import csv

# # sys - це стандартна бібліотека Python, яка дає доступ до системних параметрів та аргументів командного рядка
# # import sys
# # sys.argv - це список рядків, які Python отримує з командного рядка, коли ти запускаєш програму.
# print("hello, my name is", sys.argv[0])

# # statistics бібліотека для відслітковування певної статистики
# import statistics
# # statistics.mean - обчислює середнє арифметичне списку чисел
# print(statistics.mean([90,100]))

# # import імпортує всю бібліотеку
# # random бібліотека зроблена аби робити рандомні дії рандомні числа і тд
# import random
# # імпортує конкретний модуль з бібліотеки або всю якщо прописати *
# from random import choice
# # random.choice - вибирає рандомний елемент в лісті
# print(random.choice(["5","12"]))
# # random.randint - генерує рвндомне число в діапазоні даних
# print(random.randint(1,10))
# # random.shuffle - перемішує елементи в масиві в випадковий порядок
# names = random.shuffle(["Andriy", "Matviy", "Grigoriy"])
# for i in names:
#     print(i)




#
# list
#


# # () - кортеж це набір значень, який не можна змінити після створення
# a = (10,20,30)
# print(a)

# # Щоб задати більше двох "харектеристик" зіміній можна поставити словник в масив
# names = [
#     {"Name": "Andriy", "Class" : "Sigma", "Friend" : "Matviiy"},
#     # None - значить що нічого немає
#     {"Name": "Matviy", "Class" : None, "Friend" : "Andriy"},
#     {"Name": "Grigoriy", "Class" : "Ultra Sigma", "Friend" : "Python"}
# ]
#
# for name in names:
#     print(name["Name"], name["Class"], name["Friend"], sep=", ", end=".\n")

# # {} - Оголошує словник різниця між масивом в тому що він незмінний, і кожному значеню відповідає інше значення
# names = {"Andriy" : "Sigma", "Matviy" : "Friend", "Grigoriy" : "Ultra Sigma"}
# print(names["Grigoriy"])
# for i in names:
#     print(i, names[i], sep=", ")

# # [] - Оголошує масив, особливість масива в тому що він зберігає в собі кілька елементів, змінюєтьсяся
# names = ["Andriy","Matviy","Grigoriy"]
# # Рахунок в масиві починається з нуля
# print(names[0])
# for i in range(len(names)):
#     print(i + 1, names[i])




#
# cycle
#


# # Можна застосувати в функції
# def main():
#     number = numbers()
#     hello(number)
#
# def numbers():
#     # Працює цикл поки True а при False не працює
#     while True:
#         n = int(input("Write x - "))
#         if n > 0:
#             return n
#
# def hello(x):
#     for _ in range(x):
#         print("Hello, World!")
#
# main()

# while True:
#     x = int(input("Write x - "))
#     if x < 0:
#         # continue продовжує цикл тобто не вводить ніякі зміни
#         continue
#     else:
#         # break зупиняє цикл
#         break

# # Виконує певну дію задану кількість раз (Данний цикл можна замінити print("Hello, World!\n" * 3))
# for i in range(3):
#     print("Hello, World!")

# # while Працює, поки умова істинна
# i = 0
# while i < 3:
#     print("Hello, World!")
#     # x += 1 скорочений запис x = x + 1 так зі всіма операторами дій
#     i += 1




#
# If,else,elif, match, try, assert
#


# # assert - перевіряє чи твердження дійсне якщо ні то виводить AssertionError
# x = 5
# assert x > 0
# print("Все добре!")


# # Error
# try:
#     x = int(input("Write x - "))
# # Умова виконається якщо буте ValueError
# except ValueError:
#     # pass - означає що просто пропуститься дія
#     pass
# else:
#     print(f"x is {x}")

# # match це оператор, який порівнює значення зі даними
# name = input("Write your name - ")
# match name:
#     case "Andriy":
#         print("You sigma")
#     case "Matviy":
#         print("You friend")
#     # | виконує роль або
#     case "Grigoriy" | "Youriy" | "Pineappe":
#         print("You really sigma")
#     # _ виконує роботу коли немає такого значення в списку даних завжди пишеться в кінці
#     case _:
#         print("I don't know")

# if можна записати в функцію
# x = int(input("Write x - "))
# def main(x):
#     # % ділить числа та виводить остачу після ділення
#     return True if x % 2 == 0 else False
#     # хоча можна зробити те саме але без if
#     return x % 2 == 0
#
# print(main(x))

# # if можна ставити умови чи дорівнює функія або строка
# name = input("Write name - ")
#
# if name == "Andriy":
#     print("Your sigma")

#if - означає якщо elif - це ще одна умова якщо в одному if і else це пише якщо не співпадає ні одна наведена умова
# x = int(input("Write x - "))
# y = int(input("Write y - "))
# if x < y:
#     print("x < y")
# elif x > y:
#     print("x > y")
# or використовується як чи типу  x < y чи x > y
# if x < y or x > y :
#     print("x not = y")
# # and використовується як і типу x < y і x > y
# if x < y and x > y :
#     print("x not = y")
# else:
#     print("x = y")





#
#  function
#


# # lambda - це коротка функція в один рядок яка одразу з вбудованим return
# square = lambda a: a ** 2
# print(square(2))

# # Автоматичний запуск функції лише в цьому файлі
# def main():
#     print("Програма запущена напряму!")
#
# if __name__ == "__main__":
#     main()


# # return повертає значення з зміної
# def main():
#     x = int(input("Write x - "))
#     print("x squared is", square(x))
# # pow() підносить до вказаного степеня
# def square(x):
#     return pow(x, 2)
#
# main()

# # Застосувавши таку структуру можна поставити функцію в кінці коду
# def main():
#     name = input("Your name - ")
#     hello(name)
#
# def hello(to="world"):
#     print("Hello", to)
#
# main()


# name = input("Your name - ") #.strip().title()
# # Щоб написати функцію потрібно написати def та всередині написати її структуру
# def hello():
#     print("Hello")
# print(name)
# # В функції можна використати аргументи для прописання дій з функціями строками або числами
# def hello(to):
#     print("Hello", to)
# # якщо значення аргументу не присвоєне то воно може бути автоматичним при вказані його в функції
# def hello(to="world"):
#     print("Hello", to)
# hello(name)




#
# Number
#


# # Також в round можна ввести скільки чисел після коми залишется або написати f"{z:.2f}"
# z = round(float(input("Write x - ")) + float(input("Write y - ")), 2)
# print(z)

# # :, розділяє тисячі комами(1,000)
# z = round(float(input("Write x - ")) + float(input("Write y - ")))
# print(f"{z:,}")

# # round заокруглює дріб якщо він є
# z = round(float(input("Write x - ")) + float(input("Write y - ")))
# print(z)

# # float залишає дробову частину на відміну від int
# print(float(input("Write x - ")) + float(input("Write y - ")))

# # Задля скорочення можна писати операції одразу в зміній або print
# print(int(input("Write x - ")) + int(input("Write y - ")))

# # int відкидає дробову частинку якщо вона є і не приймає текст
# x = int(input("Write x - "))
# print(x)

# # Для математичних операцій є символи /*+- поділити, помножити, додати, відняти відповідно
# x = 1
# y = 2
# z = x*y
# print(z)




#
# STR
#


# # sorted() - сорторує данні за даним заначеня автоматично за абеткою або за порядком спадання
# names = []
#
# for _ in range(3):
#     names.append(input("Write your name - "))
#
# for name in sorted(names):
#     print(f"Hi, {name}")

# Методи

# name = input("Your name - ")
# # Метод .strip() забирає відступи на початку рядка та вкінці
# name = name.strip()
# # Метод .capitalize() пише перше слово з великої літери
# name = name.capitalize()
# # Метод .title() ише всі слова з великої літери
# name = name.title()
# # Метод .split() видає масив з видаленим символом або строкою яка вказана в методі
# name = name.split(" ")
# # Метод .join() додає в строку елементи масива
# name = "".join(name)
# # Щоб одна функція отримала кілька методів одним рядком потрібно записати їх в ряд
# name = name.strip().title()
# # Методи можна застосовувати одразу до функції коли вона вводиться
# name = input("Your name - ").strip().title()
# print(f"Hi, {name}")

# # Щоб вивести функцію всередині лапок print потрібно перед лапками поставити f і назву функції закрити в {}
# name = input("Your name - ")
# print(f"Hi, {name}")
# # Аби вивести лапки в print потрібно поставити \ перед лапками або використати лапки різних типів ('',"")
# print("Hi, \"Mr. Den\"")

# name = input("Your name - ")
# # end="" - робить так що те введеться в нього буде виведено в кінці рядка.
# # \n - робить преренесення на наступний рядок
# print("Hi", end=",\n")
# print(name)
# # sep виводить між обєктами те що в ньому введене крім кінцевого
# print("1","2","3", sep=", ")

# # При використанні + в print елементи роблять відступ один від одного.
# name = input("Your name - ")
# print("Hi," + name)