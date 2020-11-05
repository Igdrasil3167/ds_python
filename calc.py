while True:
    try:
        a = int (input("Введите первое число:"))
        b = int (input("Введите второе число:"))
        operation =input("ВВедите символ операции(+,-,*,/,^):")
    except ValueError:
        print("Нужно ввести число!")
        break
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
        print(f"{res}")