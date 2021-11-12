# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#    Проверьте его работу на данных, вводимых пользователем.
#    При вводе пользователем нуля в качестве делителя программа
#    должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionException(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

    def __str__(self):
        return self.error_text


try:
    divisible = float(input("Введите первое число >>> "))  # делимое
    divider = float(input("Введите второе число >>> "))  # делитель
    total = divisible / divider
    print(f"Результат деления: {divisible} / {divider} = {round(total, 2)}")

    if total == 0:
        raise ZeroDivisionException("0")

except ZeroDivisionException as zero:
    print(f"Деление на {zero.error_text}!")
except ZeroDivisionError:
    print(f"Деление на ноль!")
except ValueError:
    print("Ошибка! Введите только число!")
