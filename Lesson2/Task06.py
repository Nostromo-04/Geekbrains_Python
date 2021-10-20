# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#    Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
#    и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
#    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#    Пример готовой структуры:
#
#    [
#         (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#         (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#         (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#    ]
#    Необходимо собрать аналитику о товарах.
#    Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
#    а значение — список значений-характеристик, например список названий товаров.
#    Пример:
#
#    {
#    “название”: [“компьютер”, “принтер”, “сканер”],
#    “цена”: [20000, 6000, 2000],
#    “количество”: [5, 2, 7],
#    “ед”: [“шт.”]
#    }

counter = 0
input_list = []
user_count = int(input("Сколько товаров хотите добавить? "))
while counter < user_count:
    print("**********************************************")
    input_dict = {                                             # вводим данные в словарь
        "название": input("Введите наименование товара >>> "),
        "цена": input("Введите цену товара >>> "),
        "количество": input("Введите количество товара >>> "),
        "ед": "шт."}
    input_tupl = (counter + 1, input_dict) # из словаря заполняем кортеж
    input_list.append(input_tupl) # в список добавляем кортежи
    counter += 1
print("**********************************************")
print(f"Сруктура данных «Товары»: {input_list}")

output_dict = {} # создаем пустой словарь
for stroka in input_list: # получаем заполненую строку из списка
    for key, value in stroka[1].items(): # получаем из строки ключ/значение
        if key in output_dict: # если ключ есть в словаре
            if value not in output_dict.get(key): # если значение нет в словаре(по ключу)
                output_dict.get(key).append(value) # получить ключ и добавить к нему значение
        else:
            output_dict.update({key: [value]}) # добавляем ключ/значение в словарь
print(f'Собранная аналитика «Товары»: {output_dict}')