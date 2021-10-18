# 2. Для списка реализовать обмен значений соседних элементов, т.е.
#    Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#    При нечетном количестве элементов последний сохранить на своем месте.
#    Для заполнения списка элементов необходимо использовать функцию input().

user_input = input("Введите любое количество чисел до 10 >>>> ")
user_list = list(user_input)
print(f"Ваш список до:    {user_list}")
count = 0
while True:
    if count >= len(user_list) - 1:
        break
    else:
        user_list[count], user_list[count + 1] = user_list[count + 1], user_list[count]
    count += 2
print(f"Ваш список после: {user_list}")
