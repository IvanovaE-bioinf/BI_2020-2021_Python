print("Конвертер величин (массы, площади, температуры).")
my_num = float(input("Введите значение: "))
magnitude = int(input("Введите физическую величину (масса - 1, площадь - 2, температура - 3): "))

if magnitude == 1:

    d = {'кг': 1, 'г': 1000, 'мг': 1000000, 'мкг': 1000000000, 'ц': 0.01, 'т': 0.001}  # коэффициенты пересчета
    my_num_units = input("Введите единицы измерения (кг, г, мг, мкг, ц, т): ")

    if my_num_units not in d:  # проверка вводимых единиц измерения
        print("Неподдерживаемые единицы измерения!")
    else:
        SI = my_num / d[my_num_units]
        '''if my_num_units == "кг":
            
            SI = my_num  # потому что кг - это единица массы в системе СИ
        elif my_num_units == "г":
            SI = my_num * 0.001  # если другие, то пересчитываем сначала в единицы СИ
        elif my_num_units == "мг":
            SI = my_num * 0.000001
        elif my_num_units == "мкг":
            SI = my_num * 0.000000001
        elif my_num_units == "ц":
            SI = my_num * 100
        elif my_num_units == "т":
            SI = my_num * 1000'''
        print(my_num, my_num_units, "- это:")
        for key in d:  # перебираем ключи, пропуская исходные единицы измерения
            if key != my_num_units:
                print(d[key] * SI, key)
            else:
                continue

elif magnitude == 2:

    d = {'м^2': 1, 'км^2': 0.000001, 'га': 0.0001, 'а': 0.01, 'дм^2': 100, 'см^2': 10000, 'мм^2': 1000000}
    my_num_units = input("Введите единицы измерения (км^2, м^2, га, а, дм^2, см^2, мм^2): ")

    if my_num_units not in ["км^2", "м^2", "га", "а", "дм^2", "см^2", "мм^2"]:
        print("Неподдерживаемые единицы измерения!")
    else:
        if my_num_units == "м^2":
            SI = my_num
        if my_num_units == "км^2":
            SI = my_num * 1000000
        elif my_num_units == "га":
            SI = my_num * 10000
        elif my_num_units == "а":
            SI = my_num * 100
        elif my_num_units == "дм^2":
            SI = my_num * 0.01
        elif my_num_units == "см^2":
            SI = my_num * 0.0001
        elif my_num_units == "мм^2":
            SI = my_num * 0.000001
        print(my_num, my_num_units, "- это:")
        for key in d:
            if key != my_num_units:
                print(d[key] * SI, key)
            else:
                continue

elif magnitude == 3:

    my_num_units = input("Введите единицы измерения (град_Ц, град_К, град_Ф): ")

    if my_num_units == "град_Ц":  # пересчет по формулам
        print(my_num, my_num_units, "- это:")
        print(my_num + 273.15, "град_К")
        print(my_num * (9 / 5) + 32, "град_Ф")
    elif my_num_units == "град_К":
        print(my_num, my_num_units, "- это:")
        print(my_num - 273.15, "град_Ц")
        print((my_num - 273.15) * (9 / 5) + 32, "град_Ф")
    elif my_num_units == "град_Ф":
        print(my_num, my_num_units, "- это:")
        print((my_num - 32) * (5 / 9), "град_Ц")
        print((my_num - 32) * (5 / 9) + 273.15, "град_К")
    else:
        print("Неподдерживаемые единицы измерения!")
else:
    print("Неподдерживаемая физическая величина!")
