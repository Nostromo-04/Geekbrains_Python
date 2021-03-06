# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#    В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv # вызываем sys и из него импортируем только argv

unknown, num_hours, rate_hours, cash_bonus = argv # указываем какие переменные обрабатывает argv


def salary_calculate(num_hours, rate_hours, cash_bonus): # функция расчета зарплаты
    try: # попытка
        salary_total = (num_hours * rate_hours) + cash_bonus # формула расчета зарплаты
    except ValueError: # исключение
        return f"Ошибка: не заполнены параметры. Подсказка в конце скрипта." # Сообщение об ошибке
    return salary_total # возврат расчета зарплаты


salary_print = salary_calculate(int(num_hours), int(rate_hours), int(cash_bonus)) # передаем в функцию аргументы,
# возвращаемое значение записываем в переменную, для того чтобы ее использовать в выводе
print(f"Расчет заработной платы выполнен:\nВы отработали: {num_hours} часов,\nПри ставке за час: {rate_hours} $,"
      f"\nВаша премия состаила: {cash_bonus} $,\nИтого к получению: {salary_print} $")# Вывод расчета зарплаты

# Для запуска скрипта с параметрами проверьте: на коде щелкаете правой кнопкой мыши и в появившемся меню
# выбираете строку Modify Run Configuration. В открывшемся окне проверяете заполнение строки Parameters:
# пример заполнения строки 80 10 155
