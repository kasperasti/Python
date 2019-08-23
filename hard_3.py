# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player = {"name": input("Введите имя игрока: "),
          "health": 100,
          "damage": 50}
enemy = {"name": input("Введите имя соперника: "),
         "health": 100,
         "damage": 50}

def attack(player, enemy):
    if player["health"] > 0:
        enemy["health"] = enemy["health"] - player["damage"]
    else:
        print(player["name"] + " проиграл!")
    if enemy["health"] > 0:
        player["health"] = player["health"] - enemy["damage"]
    else:
        print(enemy["name"] + " проиграл!")
    return ()

while player["health"] > 0 and enemy["health"] > 0:
    attack(player, enemy)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


player = {"name": input("Введите имя игрока: "),
          "health": 100,
          "damage": 50,
          "armor": 1.2}
enemy = {"name": input("Введите имя соперника: "),
         "health": 100,
         "damage": 50,
         "armor": 1.2}

def armor(player, enemy):
    player["damage"] = round(player["damage"] / enemy["armor"])
    enemy["damage"] = round(enemy["damage"] / player["armor"])

armor(player, enemy)

def attack(player, enemy):
    # armor(player, enemy)
    if player["health"] > 0:
        enemy["health"] = enemy["health"] - player["damage"]
    else:
        print(player["name"] + " проиграл!")
    if enemy["health"] > 0:
        player["health"] = player["health"] - enemy["damage"]
    else:
        print(enemy["name"] + " проиграл!")
    return ()

while player["health"] > 0 and enemy["health"] > 0:
    attack(player, enemy)

if player["health"] < 0:
    print(player["name"] + " проиграл!")
elif enemy["health"] < 0:
    print(enemy["name"] + " проиграл!")
else:
    pass
