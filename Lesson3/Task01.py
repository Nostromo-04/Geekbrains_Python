# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dividing_numbers(num1, num2):
    try:
        div_result = num1 / num2
        return div_result
    except ZeroDivisionError:
        return f"Деление на ноль!"


print(dividing_numbers(int(input("Введите первое число >>> ")), int(input("Введите второе число >>> "))))
