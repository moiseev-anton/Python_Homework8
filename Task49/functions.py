def show_data() -> None:
    # Выводит информацию из справочника
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    # Добаляет информацию в справочник
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(enter_contact()) # Сократил код


def find_data() -> str:
    # Печатает результат поиска по справочнику.
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data = data.split('\n')
    data_to_find = input('Найти: ')
    result = search(data, data_to_find)
    print(result)
    return result # Добавил return чтобы задействовать функцию в change_data (53 строка)


def search(book: list, info: str) -> str:
    # Находит в списке записи по определенному критерию поиска
    result = [contact for contact in book if info in contact]

    if len(result) == 0:
        return 'Совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    else:
        # Если после предыдущего поиска мы получим несколько вариантов и среди них
        # мы явно видим нужный, то можем просто выбрать его из списка и не производить
        # уточняющий поиск.  Так же это поможет в ситуации если встретятся дубликаты.
        while True: # Зациклил, пока ввод не будет корректный
            print('Выберите один из найденых контактов или уточните поиск:')
            for i, contact in enumerate(result, 1): 
                print(f'{i}. {contact}') # Выводим нумерованный список с результатами поиска
            print(f'{len(result)+1}. Уточнить поиск') # Под последним номером предлагаем уточнить поиск
            choice = int(input())
            if 0 < choice <= len(result):
                return result[choice - 1]
            elif choice == len(result)+1:
                request = input('Уточнение: ')
                return search(result, request)
            else:
                print("Ошибка ввода. Попробуйте снова")
        

def change_data() -> None:
    # Удаляет или изменяет контакт в справочнике
    contact = find_data()
    if contact == 'Совпадений не найдено':
        return
    else:
        print('1. Удалить, 2. Заменить')
    choice = int(input())
    if choice == 1:
        replace_contact(contact, '') # При удалении контакта соответсвующий элемент строки из файла просто заменится на пуcтую строку
    elif choice == 2:
        replace_contact(contact, enter_contact()) 


def replace_contact(old_contact: str, new_contact: str) -> None:
    # Считывает файл в строку, заменяет фрагмент строки и перезаписывает файл
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    data = data.replace(('\n' + old_contact), new_contact)

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(data)
    print('Изменения внесены')


def enter_contact() -> str:
    # Ввод данных
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: +7')
    return (f'\n{fio} | +7{phone}')