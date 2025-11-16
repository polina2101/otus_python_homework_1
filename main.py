import csv
import os

file_path = "phone_book.csv"

def show_contacts():
    with open(file_path, "r", encoding="utf-8") as file:
        line = file.read()
        print(line)

def _search_contact(name):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            # пропускаем названия столбцов:
            if i == 0:
                continue
            if name in row:
                return i, row
        return -1, None

def find_contact():
    search = input("Введите имя: ")

    i, row = _search_contact(search)
    if i == -1:
        print("Контакт не найден")
        return
    print(row)

def create_contact():
    name = str(input("Введите имя: "))
    i, _ = _search_contact(name)
    if i != -1:
        print("Контакт с таким именем существует")
        return
    phone = input("Введите телефон: ")
    note = input("Введите заметку: ")
    data = [name, phone, note]

    with open(file_path, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        print("Контакт успешно сохранен")

def update_contact():
    search = input("Введите имя: ")

    i, contact = _search_contact(search)
    if i == -1:
        print("Контакт не найден")
        return

    rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    number = input("Измените номер телефона: ")
    note = input("Введите заметку: ")
    if number != "":
        contact[1] = number
    if note != "":
        contact[2] = note

    rows[i] = contact

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
        print("Контакт обновлен")

def delete_contact():
    search = input("Введите имя: ")

    i, contact = _search_contact(search)
    if i == -1:
        print("Контакт не найден")
        return

    rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    del rows[i]

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
        print("Контакт удален")

def main():
    if not os.path.exists(file_path):
        print(f"Книжка '{file_path}' не найдена.")
        return

    while True:
        menu = input(""" 
            Для продолжения введите цифру:
            1 - Показать все контакты
            2 - Найти контакт
            3 - Создать контакт
            4 - Изменить существующий контакт
            5 - Удалить контакт
            6 - Выйти из книги
        """)
        if menu == "1":
            show_contacts()
        elif menu == "2":
            find_contact()
        elif menu == "3":
            create_contact()
        elif menu == "4":
            update_contact()
        elif menu == "5":
            delete_contact()
        elif menu == "6":
            break
        else:
            print(f"Неизвестная команда: {menu}")

if __name__ == "__main__":
    main()