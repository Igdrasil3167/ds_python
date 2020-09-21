#условные операторы

a = 410

if a==5:
    c = "Равно 5"
elif a == 4:
    c = "Равно 4"
elif a == 3:
    c = "Равно 3"
elif a == 2:
    c = "Равно 2"
elif a == 1:
    c = "Равно 1"
else:
    "Ничему не равно"




b = 11
if b < 10 and  b > 0:
    c = "0 < b < 10" 
# elif b > 0
#  c = "> b"
else:
    c = "b больше 10 либо меньше 0"

x = True

#if not x:
#    print ("Foo")
#else:
#    print ("Bar")

#****** Простой калькулятор ******

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