

import os.path
import csv

def export_data():
    if not os.path.exists("Phonebook.csv"):
        with open("Phonebook.csv", "w", encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=";")
            writer.writerow(("Фамилия", "Имя", "Номер телефона", "Комментарии"))
    exit = ""
    while exit != "q":
        user_data = [
            input('введите фамилию: '),
            input('введите имя: '),
            input('введите номер телефона: '),
            input('введите комментарии: ')
        ]
        with open('Phonebook.csv', 'a', encoding='utf-8') as dt:
            dt.write(f'{user_data[0]};{user_data[1]};{user_data[2]};{user_data[3]} \n')

        with open('Phonebook.txt', 'a', encoding='utf-8') as dt:
            dt.write(
                f'Фамилия: {user_data[0]}\n Имя: {user_data[1]}\n\n номер телефона: {user_data[2]}\n\n Комментарии: {user_data[3]}\n\n\n')

        exit = input('Создана новая запись в телефонной книге.\n\nДля выхода из телефонной книги нажмите "q"\n Для продолжения нажмите "Enter"\n')
