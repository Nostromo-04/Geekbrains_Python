# 3. Реализовать базовый класс Worker (работник),
#    в котором определить атрибуты: name, surname, position (должность), income (доход).
#    Последний атрибут должен быть защищенным и ссылаться на словарь,
#    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#    Создать класс Position (должность) на базе класса Worker.
#    В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#    и дохода с учетом премии (get_total_income).
#    Проверить работу примера на реальных данных
#    (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:  # родительский класс
    name: str
    surname: str
    position: str
    _income = dict(wage='wage', bonus='bonus')

    def __init__(self, name, surname, position, wage, bonus):  # конструктор объекта
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):  # дочерний класс

    def get_full_name(self):  # метод
        return f"{self.name} {self.surname}"

    def get_total_income(self):  # метод
        return self._income["wage"] + self._income["bonus"]


position_1 = Position("Пётр", "Первый", "Царь", 1000, 200)  # экземпляр класса

print(f"Имя: {position_1.name}")  # вызов метода
print(f"Фамилия: {position_1.surname}")
print(f"Должность: {position_1.position}")
print(f"Метод get_full_name: {position_1.get_full_name()}")
print(f"Метод get_total_income: {position_1.get_total_income()}")
