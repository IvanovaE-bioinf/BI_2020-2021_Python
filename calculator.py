number_1 = float(input("Enter a number: "))
operator = input("Enter an operator: ")
number_2 = float(input("Enter a number: "))
if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "/":
    if number_2 == 0:
        print("Invalid operation - division by zero!")
    else:
        print(number_1 / number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "//":
    print(number_1 // number_2)
elif operator == "%":
    print(number_1 % number_2)
else:
    print("Mission impossible - invalid operator!")