# Задание 1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

basketball_players = {}

def add(name, height):
    basketball_players[name] = height
    print(f"Баскетболист {name} с ростом {height} см добавлен.")

def remove(name):
    if name in basketball_players:
        del basketball_players[name]
        print(f"Баскетболист {name} удален.")
    else:
        print(f"Баскетболист с именем {name} не найден.")

def find(name):
    if name in basketball_players:
        print(f"Баскетболист {name} найден: рост {basketball_players[name]} см.")
    else:
        print(f"Баскетболист с именем {name} не найден.")

def update(name, new_height):
    if name in basketball_players:
        basketball_players[name] = new_height
        print(f"Данные баскетболиста {name} обновлены: новый рост {new_height} см.")
    else:
        print(f"Баскетболист с именем {name} не найден.")

def show():
    if basketball_players:
        print("Список всех баскетболистов:")
        for name, height in basketball_players.items():
            print(f"Имя: {name}, Рост: {height} см")
    else:
        print("Список баскетболистов пуст.")

add("Майкл Джордан", 198)
add("Леброн Джеймс", 206)
add("Билли Ганн", 195)
show()

find("Майкл Джордан")

update("Леброн Джеймс", 207)
show()

remove("Майкл Джордан")
show()