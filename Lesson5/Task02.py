# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
#    выполнить подсчет количества строк, количества слов в каждой строке.

# Блок создания файла закоментрировал, так как файл нужно создать в ручную.
# with open('task02.txt', 'w') as my_files:  # менеджер контекста - открываем на запись
#     my_files.write("First string\n")  # запись строки в файл
#     my_files.write("Second string string\n")  # запись строки в файл
#     my_files.write("Last string string string\n")  # запись строки в файл

with open('task02.txt') as my_files:  # менеджер контекста - открываем на чтение
    for idx, el in enumerate(my_files, 1):  # цикл, перебираем строки в файле
        print(f"Найдено: {idx} строка")  # вывод
    print(f"Всего в файле {idx} строки")  # вывод

print("*" * 25)  # разделительная строка
with open('task02.txt') as my_files:  # менеджер контекста - открываем на чтение
    counter = 1  # счетчик
    file_list = my_files.readlines()  # читаем из файда все строки
    for word in file_list:  # цикл, перебираем строки
        print(f"{counter} строка: {word.split()}")  # вывод
        print(f"В {counter} строке {len(word.split())} слова")  # вывод
        counter += 1  # счетчик
