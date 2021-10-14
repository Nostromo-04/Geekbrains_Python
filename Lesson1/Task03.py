# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

digit = input("Введите любое число до 10 >>>")
o_digit = int(digit)
two_digit = digit + digit
t_digit = int(two_digit)
three_digit = digit + digit + digit
th_digit = int(three_digit)
total = int(o_digit + t_digit + th_digit)
print(f"{o_digit} + {t_digit} + {th_digit} = {total}")

