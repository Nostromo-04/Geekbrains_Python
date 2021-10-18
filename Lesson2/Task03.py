# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#    Напишите решения через list и через dict.

# 1.ВАРИАНТ через list
user_input = int(input("Введите число месяца >>>> "))
seasons = ["ЗИМЕ", "ВЕСНЕ", "ЛЕТУ", "ОСЕНИ"]
if user_input == 12 or user_input == 1 or user_input == 2:
    print(f"Выбранный месяц относится к {seasons[0]}")
elif user_input == 3 or user_input == 4 or user_input == 5:
    print(f"Выбранный месяц относится к {seasons[1]}")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print(f"Выбранный месяц относится к {seasons[2]}")
else:
    print(f"Выбранный месяц относится к {seasons[3]}")

# 2.ВАРИАНТ через dict
user_input = int(input("Введите число месяца >>>> "))
seasons = {1: "ЗИМЕ", 2: "ВЕСНЕ", 3: "ЛЕТУ", 4: "ОСЕНИ"}
if user_input == 12 or user_input == 1 or user_input == 2:
    print(f"Выбранный месяц относится к {seasons.get(1)}")
elif user_input == 3 or user_input == 4 or user_input == 5:
    print(f"Выбранный месяц относится к {seasons.get(2)}")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print(f"Выбранный месяц относится к {seasons.get(3)}")
else:
    print(f"Выбранный месяц относится к {seasons.get(4)}")
