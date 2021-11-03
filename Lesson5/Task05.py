# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task05.txt', 'w') as my_files:  # менеджер контекста - открываем на запись
    my_files.write("1 2 3 4 5 6 7 8 9")  # запись строки в файл

with open('task05.txt') as my_files:  # менеджер контекста - открываем на чтение
    sum_num = 0  # переменная, в которую будет записана сумма
    for el in my_files:  # цикл, перебор строк в файле
        num_list = el.split()  # разбиваем строку на цифры
        for x in num_list:  # цикл, перебираем цифры
            sum_num += int(x)  # суммируем цифры
    print(f"Числа из файла: {num_list}")  # вывод
    print(f"Сумма чисел равна {sum_num}")  # вывод