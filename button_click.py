
import export_data as exp
import import_data as imp
import view
import log

def button_click():
    choise = view.button()
    while choise != "q":
        log.log_info(choise)
        if choise == "1":
            exp.export_data()
        elif choise == "2":
            what_find = input("Для поиска по фамилии введите '1'\n Для поиска по имени введите '2'\n ")
            if what_find == '1':
                imp.find_surname(input('Введите фамилию: '))
            if what_find == '2':
                imp.find_name(input('Введите имя: '))
        else:
            print("Такой команды нет")
        choise = view.button()

