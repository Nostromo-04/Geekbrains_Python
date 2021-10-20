# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы.
#    Реализовать вывод данных о пользователе одной строкой.

def user_data(first_name, last_name, year_of_birth, city, email, phone):
    return print(
        f"Ф.И.О: {last_name} {first_name}, {year_of_birth} г.р., город проживания {city}, email: {email}, телефон: {phone}")


user_data(
    first_name=input("Имя: "),
    last_name=input("Фамилия: "),
    year_of_birth=input("год рождения: "),
    city=input("город: "),
    email="red_square@mail.ru ",
    phone="+7 707 010 010 1")
