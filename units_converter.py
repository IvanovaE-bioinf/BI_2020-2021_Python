print("Введите значение и единицы измерения:")
print('(кг, г, мг, мкг, ц, т; м^2, км^2, га, а, дм^2, см^2, мм^2; Ц, К, Ф)')
my_num, my_num_units = input().split()
my_num = float(my_num)
# коэффициенты пересчета
d1 = {'кг': 1,
      'г': 1000,
      'мг': 1000000,
      'мкг': 1000000000,
      'ц': 0.01,
      'т': 0.001}
d2 = {'м^2': 1,
      'км^2': 0.000001,
      'га': 0.0001,
      'а': 0.01,
      'дм^2': 100,
      'см^2': 10000,
      'мм^2': 1000000}
d3 = ['Ц', 'К', 'Ф']

if my_num_units in d1:
    SI = my_num / d1[my_num_units]  # перевод в единицу массы в системе СИ
    print(my_num, my_num_units, "- это:")
    for key in d1:  # перебираем ключи, пропуская исходные единицы измерения
        if key != my_num_units:
            print(d1[key] * SI, key)
        else:
            continue

elif my_num_units in d2:
    SI = my_num / d2[my_num_units]
    print(my_num, my_num_units, "- это:")
    for key in d2:  # перебираем ключи, пропуская исходные единицы измерения
        if key != my_num_units:
            print(d2[key] * SI, key)
        else:
            continue

elif my_num_units in d3:  # пересчет по формулам
    if my_num_units == "Ц":
        print(my_num, my_num_units, "- это:")
        print(my_num + 273.15, "К")
        print(my_num * (9 / 5) + 32, "Ф")
    elif my_num_units == "К":
        print(my_num, my_num_units, "- это:")
        print(my_num - 273.15, "Ц")
        print((my_num - 273.15) * (9 / 5) + 32, "Ф")
    elif my_num_units == "Ф":
        print(my_num, my_num_units, "- это:")
        print((my_num - 32) * (5 / 9), "Ц")
        print((my_num - 32) * (5 / 9) + 273.15, "К")

else:
    print("Неподдерживаемые единицы измерения!")
