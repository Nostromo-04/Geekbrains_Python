# 5. Запросите у пользователя значения выручки и издержек фирмы.
#    Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
#    или убыток — издержки больше выручки). Выведите соответствующее сообщение.
#    Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введи сумму выручки >>>>"))
expenses = int(input("Введи сумму издержек >>>>"))
profit = int(0)
if revenue > expenses:
    print("Прибыль больше расходов.")
    profit = (revenue - expenses) / revenue
    print("Рентабельность составила", "%.2f" % profit, "%")
    num_staff = int(input("Введите количество сотрудников >>>>"))
    pers_profit = profit / num_staff
    print("Прибыль на каждого сотрудника составила", "%.2f" % pers_profit, "%")
else:
    print("Расходы больше прибыли.")



