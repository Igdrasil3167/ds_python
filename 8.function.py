
# *** Функции ***

# Функции - это обычно "фабрики", которые на вход принимают какие-либо данные и на выход возвращают другие данные

# 1 вариант. Функция, которая на вход ничего не принимает и на выход ничего не возвращает

def func_1():
	print("Hello World!")

def func_2():
	name = "Aiyyskhan"
	print(f"Hello {name}!")


# 2 вариант. Функция, которая принимает данные (имеет вход(-ы) (аргументы)), но не ничего не возвращает

def func_3(argument_1, arg_2):
	result = argument_1 + arg_2
	print(result)

# вызов функции с передачей параметров аргументам
# func_3(100, 55)

# 2.1 вариант. Функция, принимающая данные, но не ничего не возвращает 
# аргументы имеют значения по умолчанию

def func_4(arg_1, arg_2, arg_3=10):
	result = arg_1 + arg_2 * arg_3
	print(result)

# func_4(100, 20, 5)

# 2.2 вариант. Функция, принимающая данные, но не ничего не возвращает 
# позиционные параметры

def func_5(arg_1=10, arg_2=20, arg_3=30):
	result = arg_1 + arg_2 + arg_3
	print(result)

# func_5(2, 3, 4)
# func_5(100, 20)

# 2.3 вариант. Функция, принимающая данные, но не ничего не возвращает 
# именованные параметры

def func_6(arg_1=10, arg_2=20, arg_3=30):
	result = arg_1 + arg_2 + arg_3
	print(result)

# func_6(arg_3=100, arg_1=5)

# 2.4 вариант. Функция, принимающая данные, но не ничего не возвращает 
# множественные позиционные параметры

def func_7(*args):
	"""
	docstring
	"""
	print(args)

# можно передавать произвольное количество позиционных параметров
# они будут упакованы в виде кортежа
# func_7(10, 29, 30)

def func_8(*args):
	"""
	функция, которая складывает произвольное количество параметров 
	"""
	result = 0
	for num in args:
		result += num
	print(result)

# func_8(100, 200)

# 2.5 вариант. Функция, принимающая данные, но не ничего не возвращает 
# множественные именованные параметры

def func_9(**args):
	print(args)

# можно передавать произвольное количество именованных параметров
# они будут упакованы в виде словаря
# func_9(x=100, y=200, z=300)

# импортируем математический модуль
import math

def distance_calculate(**args):
	"""
	функция, которая вычисляет дистанцию от начала координат (0,0,0) до точки с координатами (x,y,z)
	"""
	# переменная keys будет хранить список ключей аргументов из args
	keys = list(args.keys())
	
	# для вычисления дистанции применяем теорему Пифагора
	summa = 0

	# извлекаем все ключи из списка ключей
	for axis in keys:
		# суммирование квадратов катетов (значений координатных осей)
		summa += args[axis] ** 2

	# извлечение квадратного корня
	distance = math.sqrt(summa)

	print(f"Дистанция: {distance}")

# Вызов функции
# distance_calculate(x=10, y=20, z=10, a=5)


# Вариант 3. Функция, которая принимает и возвращает данные

def func_10(x, y):
	summa = x + y
	return summa

# Вызов функции и присвоения возвращаемого значения в переменнную 
result = func_10(10, 20)

# print(result)

# Передача возвращаемого значения из одной функции в другую "на лету"
# print(func_10(10, 20))

# Функция, возвращающая 2 значения
def func_11(x, y):
	res_1 = x ** 2
	res_2 = y ** 3
	return res_1, res_2

# print(func_11(2, 4))

# Присвовение нескольких возвращаемых значений в переменные
a, b = func_11(2, 4)

# print(a, b)


# *** Безымянные функции  (лямбда - функции, лямбда выражения) ***

# создание лямбда - выражения
foo = lambda x, y: (x * y) + (x * y)

# Вызов лямбда - выражения с передачей 	параметров  и передача возвращаемого значения "на лету"
# print(foo(2, 3))

# Вызов лямбда - выражения с передачей 	параметров  и передача возвращаемого значения в переменную
res = foo(2, 2)
# print(res)

# Пример. Лямбда внутри генератора списка

my_list = [(lambda arg: arg ** 2)(i) for i in range(1, 10)]

# print(my_list)

# Примеры. Лямбда внутри списка и словаря 
lambda_list = [lambda x, y: x + y, lambda x, y: x * y]

# res = lambda_list[0](10, 20)
res = lambda_list[1](10, 20)

# print(res)

# Пример. Лямбда внутри словаря
lambda_dict = {"сумма": lambda x, y: x + y, "Произведение": lambda x, y: x * y}

res = lambda_dict["сумма"](20, 30)

# print(res)


# *** Декораторы ***

# Декорируют функции - добавляют дополнительный функционал обёрнутым функциям

# собственно функция - декоратор
def decorator(func):
	'''
	func : аргумент, которому присваивается объект целевой функции
	'''
	# Функция обёртка
	def wrapper():
		# код который выполняется ДО выполнения целевой функции
		print(foo)

		# вызывается целевая функция из агрумента
		func()

		# код который выполняется ПОСЛЕ выполнения целевой функции
		print("bar")

	# Возврат объекта функции - обёртки
	return wrapper	
		




# Присваиваем задекорированную функцию в старое название
# my_func_1 = dec(my_func_1)


# *** Новый способ применения декоратора ***

# целевые функции

@decorator
def my_func_2():
	print("hello!")

@decorator
def my_func_3():
	print("Привет!")


# Вызов задекорированной функции
# my_func_3()

# *** Декорирует функции, которая имеет аргументы и возвращает значения

def decorator_1 (func):
	def wrapper(a, b):
		print(f"ДО: {a}, {b}")
		func(a, b)
		print(f"ДО: {a*2}, {b*2}")
		return res
	return wrapper

@decorator_1
def target_func(x, y):
	return x ** y

print(target_func(10, 2))