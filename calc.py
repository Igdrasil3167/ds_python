a = int (input("Введите первое число:"))
b = int (input("Введите второе число:"))
type
operation =input("ВВедите символ операции(+,-,*,/,^):")

if operation == "+":
    res = a + b
elif operation == "-":
    res = a - b
elif operation == "*":
    res = a * b
elif operation == "/":
    res = a / b
elif operation == "^":
    res = a ** b
else:
    res ("Символ операции некорректный")

print(f"Результат: {res}")
