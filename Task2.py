# Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

dictionary = {}

def add_word(english_word, french_word):
    dictionary[english_word] = french_word
    print(f"Слово '{english_word}' добавлено с переводом '{french_word}'")

def remove_word(english_word):
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Слово '{english_word}' удалено")
    else:
        print(f"Слово '{english_word}' не найдено")

def search_word(english_word):
    if english_word in dictionary:
        print(f"Перевод для '{english_word}' - '{dictionary[english_word]}'")
    else:
        print(f"Слово '{english_word}' не найдено")

def replace_word(english_word, new_french_word):
    if english_word in dictionary:
        dictionary[english_word] = new_french_word
        print(f"Перевод для '{english_word}' заменен на '{new_french_word}'")
    else:
        print(f"Слово '{english_word}' не найдено")

while True:
    print("\nАнгло-французский словарь: ")
    print("1) Добавить слово")
    print("2) Удалить слово")
    print("3) Поиск перевода")
    print("4) Заменить перевод")
    print("5) Показать все слова")
    print("6) Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        english_word = input("Введите слово на английском: ")
        french_word = input("Введите перевод на французском: ")
        add_word(english_word, french_word)
    
    elif choice == "2":
        english_word = input("Введите слово на английском для удаления: ")
        remove_word(english_word)
    
    elif choice == "3":
        english_word = input("Введите слово на английском для поиска: ")
        search_word(english_word)
    
    elif choice == "4":
        english_word = input("Введите слово на английском для замены: ")
        new_french_word = input("Введите новый перевод на французском: ")
        replace_word(english_word, new_french_word)
    
    elif choice == "5":
        if dictionary:
            print("\nВсе слова в словаре: \n(english - french):")
            for english, french in dictionary.items():
                print(f"{english} - {french}")
        else:
            print("Словарь пуст")
    
    elif choice == "6":
        print("Выход из программы")
        break
    
    else:
        print("Неверный выбор")