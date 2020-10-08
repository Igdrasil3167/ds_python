# *** Циклы (операторы циклов) ***

# *** Оператор цикла while ***

number = 0

# "Ctrl + /" - закомментировать/раскомментировать

# while number <= 10:
# 	print(number)
# 	number += 1 # number = number + 1

# прерывание цикла по дополнительному условию
# while number < 10:
# 	if number == 5: # если значение number станет равной 5,
# 		break	# то вызываем инструкцию break, которая прерывает цикл
# 	print(number)
# 	number += 1

# пример прерывания бесконечного цикла с использованием break
# while True:
# 	s = input("Введите команду: ")
# 	print(f"Вы ввели команду: {s}")
# 	if s.lower() == "стоп":
# 		break

# !!!!
# *** Если бесконечный цикл не вырубается,
# *** то нужно нажать сочетание клавиш "Ctrl + C" и потом нажать "Enter"
# !!!!

# пропуск куска кода из тела цикла
# while True:
# 	s = input("Введите слово 'YES': ")
# 	if s != "YES":
# 		print("Вы не ввели слово 'YES'!!! :((")
# 		continue # если вызывается инструкция continue, то цикл возвращается в начало
# 	print(f"Вы ввели команду: {s}")
# 	break


# *** Оператор цикла for ***

# 1. читает элемент по порядку
# 2. присваивает значение элемента в свою переменную
# 3. выполняет блок кода своего тела

# for n in [1,2,3,4,5,6]:
# 	print(n)

my_tuple = (100, 200, 300)

# for n in my_tuple:
# 	print(n)

# for n in my_tuple[::-1]:
# 	print(n)

# for n in my_tuple:
# 	if n == 200:
# 		break
# 	print(n)

# for idx in range(5, 20, 2):
# 	res = idx + 1
# 	print(res)


# *** Генераторы списков ***

# Создание списка с числами в диапозоне от 0 до 9
# my_list = [num for num in range (10)]

# Создание списка с числами в диапозоне от 50 до 90
# my_list = [num for num in range (50, 100, 10)]

# Создание списка с числами в диапозоне от 0 до 9 с возведением в степень 2
# my_list = [num ** 2 for num in range (10)]

# Создание списка с числами в диапозоне от 0 до 9 которые больше 5
# my_list = [num for num in range(10) if num >5]


# *** Генератор словаря ***

# *** Создание словаря из списка символов ***
my_dict = {symbol : symbol for symbol in ["a", "b", "c"]}

# *** Создание словаря из списка символов ***
list_1 =[('a', 10), ('b', 20), ('c', 30)]

my_dict = {key : val for key, val in list_1}



# *** Практическое использование циклов ***

# *** Калькулятор ***

commands = {"stop", "+", "-", "*", "/"}

while True:

	# Ввод чисел
	num_list =[]
	for i in range(2):
		num = int(input(f"Введите {i+1} число: "))
		num_list.append(num)

	# Ввод команды
	cmd = None
	while True:
		cmd = input("Введите команду: ")
		if cmd not in commands:
			print("Вы ввели неправильную команду!!! ") 
			continue
		else:
			break
	
	# Вычисление
	if cmd == 'stop':
		print("До свидание")
		break
	elif cmd == "+":
		res = num_list[0] + num_list[1]
	elif cmd == "-":
		res = num_list[0] - num_list[1]
	elif cmd == "*":
		res = num_list[0] * num_list[1]
	elif cmd == "/":
		res = num_list[0] / num_list[1]
	
	# Вывод результатов
	print(f"Результат: {res}")