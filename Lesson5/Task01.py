# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#    Об окончании ввода данных свидетельствует пустая строка.

with open('task01.txt', 'a', encoding='UTF-8') as my_files:  # менеджер контекста - открыть файл task01.txt(если его
    # не существет - создать новый), 'а' - открыть файл на дозапись(добавляет информацию в конец файла),
    # encoding='UTF-8' - кодировка, для того чтобы в файл можно было записать русские слова.

    while True:  # в цикле будет запрашивать у пользователя вводимую строку. Прерывание - пустая строка!
        user_input = input("Введите данные >>>> ")  # ввод данных
        print(user_input, file=my_files)  # через print отправляем введенную строку user_input используя стрим my_files

        if not user_input:  # если пустая строка, то
            break  # выход из цикла
