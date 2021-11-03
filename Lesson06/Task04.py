# 4.Реализуйте базовый класс Car.
#   У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
#   остановилась, повернула (куда).
#   Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#   Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#   Для классов TownCar и WorkCar переопределите метод show_speed.
#   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
#   Создайте экземпляры классов, передайте значения атрибутов.
#   Выполните доступ к атрибутам, выведите результат.
#   Выполните вызов методов и также покажите результат.

class Car:  # родительский класс
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):  # конструктор объекта
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):  # метод
        return f"Автомобиль начал движение"

    def stop(self):  # метод
        return f"Автомобиль остановился"

    def turn(self, revers):  # метод
        return f"Автомобиль поворачивает на {revers}"

    def show_speed(self, speed):  # метод
        return f"Автомобиль движется со скоростью: {speed}"


class TownCar(Car):  # дочерний класс
    def show_speed(self):  # переопределяемый метод
        if self.speed > 60:
            print(f"Скорость {self.speed} !!! Превышение скоростного режима!")
        else:
            print(f"Скорость автомобиля: {self.speed}")
        print(f"Автомобиль: {self.name}, цвет: {self.color}, скорость: {self.speed}, это полиция? {self.is_police}")


class SportCar(Car):  # дочерний класс
    def info(self):  # метод
        return f"Автомобиль: {self.name}, цвет: {self.color}, скорость: {self.speed}, это полиция? {self.is_police}"


class WorkCar(Car):  # дочерний класс
    def show_speed(self):  # переопределяемый метод
        if self.speed > 40:
            print(f"Скорость {self.speed} !!! Превышение скоростного режима!")
        else:
            print(f"Скорость автомобиля: {self.speed}")
        print(f"Автомобиль: {self.name}, цвет: {self.color}, скорость: {self.speed}, это полиция? {self.is_police}")


class PoliceCar(Car):  # дочерний класс
    def info(self):  # метод
        return f"Автомобиль: {self.name}, цвет: {self.color}, скорость: {self.speed}, это полиция? {self.is_police}"


car = Car(60, "yellow", "Taxi", False)  # экземпляр класса Car
print(car.go())
print(car.stop())
print(car.turn("лево"))
print(car.show_speed(75))
print()

t_w = TownCar(90, "green", "Vaz-2114", False)  # экземпляр класса TownCar
t_w.show_speed()  # вызов метода
print()

s_c = SportCar(350, "red", "Ferrari", False)  # экземпляр класса SportCar
print(s_c.info())  # вызов метода
print()

w_k = WorkCar(39, "blue", "Cadillac", False)  # экземпляр класса WorkCar
w_k.show_speed()  # вызов метода
print()

p_c = PoliceCar(180, "black", "GM", True)  # экземпляр класса PoliceCar
print(p_c.info())  # вызов метода
