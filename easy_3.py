# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def anketa():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    city = input("Введите город, в коротором проживаете: ")
    print(f"{name}, {age} год, проживает в городе {city}".format())
    return

anketa()

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

a = int(input("Введите любое число: "))
b = int(input("Введите любое число: "))
c = int(input("Введите любое число: "))
def max_numder():
    numbers = [a, b, c]
    print(max(numbers))
    return
max_numder()

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов



def max_len(*args):
    long_string = ""
    for el in args:
        if len(el) > len(args):
            long_string = el
            return()
