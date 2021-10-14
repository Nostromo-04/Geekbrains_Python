# 4. Пользователь вводит целое положительное число.
#    Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.

digit = int(input("Введите целое положительное число >>>>"))
big_digit = int(0)
while digit:
    if digit % 10 > big_digit:
        big_digit = digit % 10
    else:
        digit //= 10
print(big_digit)
