# 2. Пользователь вводит время в секундах.
#    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.

times = int(input("Введите время в секундах >>>>"))
if times < 86400:
    hours = times // 3600
    minutes = times % 3600 // 60
    seconds = times % 3600 % 60
    print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
else:
    print("ОШИБКА: Максимальное число 86400")
