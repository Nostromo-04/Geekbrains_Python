# 4. Создать (не программно) текстовый файл со следующим содержимым:
#    One — 1
#    Two — 2
#    Three — 3
#    Four — 4
#
#    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#    При этом английские числительные должны заменяться на русские.
#    Новый блок строк должен записываться в новый текстовый файл.

# Блок создания файла закоментрировал, так как файл нужно создать в ручную.
# with open('task04_data.txt', 'w') as my_files:  # менеджер контекста - открываем на запись
#     my_files.write("One - 1\n")  # запись строки в файл
#     my_files.write("Two - 2\n")
#     my_files.write("Three - 3\n")
#     my_files.write("Four - 4\n")

with open('task04_data.txt') as my_files:  # менеджер контекста - открываем на чтение
    for row in my_files:  # цикл, перебираем строки
        spl_row = row.split()  # разбиваем строку на слова
        if spl_row[0] == "One":  # замена
            spl_row[0] = "Один"  # значения
            one_row = f"{spl_row[0]} {spl_row[1]} {spl_row[2]}"  # склеиваем строку, как было
        elif spl_row[0] == "Two":  # замена
            spl_row[0] = "Два"  # значения
            two_row = f"{spl_row[0]} {spl_row[1]} {spl_row[2]}"  # склеиваем строку, как было
        elif spl_row[0] == "Three":  # замена
            spl_row[0] = "Три"  # значения
            trhee_row = f"{spl_row[0]} {spl_row[1]} {spl_row[2]}"  # склеиваем строку, как было
        else:
            spl_row[0] = "Четыре"  # замена значения
            four_row = f"{spl_row[0]} {spl_row[1]} {spl_row[2]}"  # склеиваем строку, как было

with open('task04_save.txt', 'w', encoding='UTF-8') as my_files:  # менеджер контекста - открываем на запись
    my_files.write(f"{one_row}\n")  # запись строки в файл
    my_files.write(f"{two_row}\n")
    my_files.write(f"{trhee_row}\n")
    my_files.write(f"{four_row}\n")
