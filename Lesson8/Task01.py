# 1. Реализовать класс «Дата»,
#    функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#    В рамках класса реализовать два метода.
#    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#    Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, dates: str):
        self.dates = dates

    def __str__(self):
        return f"Дата в формате строки: {self.dates}"

    @classmethod
    def data_number(cls, dates):
        data_list = []

        for el in dates.split("-"):
            data_list.append(el)
        cls.days = int(data_list[0])
        cls.months = int(data_list[1])
        cls.years = int(data_list[2])

        return f"Дата в формате числа: {cls.days} {cls.months} {cls.years}"

    @staticmethod
    def data_validation(days: int, months: int, years: int):

        if days > 31:
            return f"Неверная дата: {days}"
        elif months > 12:
            return f"Неверный месяц: {months}"
        elif years != 2021:
            return f"Укажите текущий год: {years}"
        else:
            return f"Вы ввели правильную дату: {days}.{months}.{years}"


day = Data("26-12-2021")

print(day)
print(day.data_number(day.dates))
print(day.data_validation(day.days, day.months, day.years))

