import csv
import os.path
import view

def find_surname(surname):
    if os.path.exists("Phonebook.csv"):
        with open("Phonebook.csv", "r", encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(";"))
            count = 0
            for item in sum_list:
                if surname == item[0]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f"{surname} не найден!")
    else:
        view.answer("Файл не найден!")

def find_name(name):
    if os.path.exists("Phonebook.csv"):
        with open('Phonebook.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(";"))
            count = 0
            for item in sum_list:
                if name == item[1]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f"{name} не найден!")
    else:
        view.answer("Файл не найден!")
