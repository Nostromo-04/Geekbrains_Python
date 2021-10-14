# 6. Спортсмен занимается ежедневными пробежками.
#    В первый день его результат составил a километров.
#    Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#    Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#    Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#    Например: a = 2, b = 3.
#    Результат:
#    1-й день: 2
#    2-й день: 2,2
#    3-й день: 2,42
#    4-й день: 2,66
#    5-й день: 2,93
#    6-й день: 3,22
#
#    Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# 1.Вариант решения задачи
# low_distance = float(input("Введите начальную дистанцию пробежки >>>> "))
# high_distance = float(input("Введите конечную дистанцию пробежки >>>> "))
# days = int(0)
# gain = float(low_distance * 10 / 100)
# while low_distance < high_distance:
#     days += 1
#     print("{}-й день: {:.2f}".format(days,low_distance))
#     low_distance = float(low_distance + gain)
# days += 1
# print("{}-й день: {:.2f}".format(days, low_distance))
# print("На {}-й день спортсмен достиг результата - не менее {:.2f} км.".format(days,high_distance))

# 2.Вариант решения задачи
low_distance = float(input("Введите начальную дистанцию пробежки >>>> "))
high_distance = float(input("Введите конечную дистанцию пробежки >>>> "))
days = int(0)
gain = float(low_distance * 10 / 100)
while True:
    if low_distance < high_distance:
        days += 1
        print("{}-й день: {:.2f}".format(days, low_distance))
        low_distance = float(low_distance + gain)
    else:
        break
days += 1
print("{}-й день: {:.2f}".format(days, low_distance))
print("На {}-й день спортсмен достиг результата - не менее {:.2f} км.".format(days,high_distance))
