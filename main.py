#calculator
import math

number_1 = input("Press the first number:")
number_2 = input("Press the second number:")
sign = input("Put right sing what you need in your math analys(+ - * /):")
result_plus = int(number_1) + int(number_2)
result_minus = int(number_1) - int(number_2)
result_multiply = int(number_1) * int(number_2)
result_divide = int(number_1) / int(number_2)

plus = "+"
minus = "-"
multiply = "*"
divide = "/"

if sign == plus:
    print(result_plus)
elif sign == minus:
    print(result_minus)
elif sign == multiply:
    print(result_multiply)
elif sign == divide:
    print(result_divide)