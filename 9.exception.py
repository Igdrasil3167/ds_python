# *** Исключения (исключительные события, искл. ситуации, ошибки, Exception) ***

# Пример ошибки "деление на ноль"

a = 100
b = 10

# без обработки потенциального исключения
# c = a / b

# обработка исключения, конструкция "try-except"
try: # попытка
	c = a / b
except:
	# код который работает при обнаружении исключительного события
	# print("Что-то пошло не так :(")
	c = 0

# print("Результат: ", c)

# val_1 = int(input("Введите число: "))
# result = 50 / val_1

# обработка множества исключений

# try:
# 	val_1 = int(input("Введите число: "))
# 	result = 50 / val_1

# # обработка конкретного исключения
# except ValueError as error:
# 	print(f"Возникло исключение: {ValueError} : {error}")
# 	print("Нужно ввести число!")
# except ZeroDivisionError:
# 	print("Попытка деления на ноль!")

# # обработка общего исключения
# except Exception as error:
# 	print(error)


# конструкция "try-except-else"

# вариант без использования else

# потенциально аварийный участок кода
# try:
# 	a = int(input("Введите число: "))
# 	c = 100 / a
# except ZeroDivisionError:
# 	c = 0

# кусок кода который должен работать в любом случае
# print("Result: ", c)

# вариант с использованием else
# try:
# 	a = int(input("Введите число: "))
# 	c = 100 / a
# except ZeroDivisionError:
# 	c = 0
# # блок else срабатывает если НЕ отлавливаются исключения
# else:
# 	print("Result: ", c)


# Конструкция "try-except-finally"

# try:
# 	a = int(input("Введите число: "))
# 	c = 100 / a
# 	print("Полет нормальный")
# except ZeroDivisionError:
# 	c = 0
# 	print("Деление на ноль")
# #  finally срабатывает в любом случае, даже если программа завершается аварийно
# finally:
# 	# внутри должны быть критически важные действия
# 	# например, закрытие файла или сессии базы данных и т.д.
# 	print("Сработала finally")

# Конструкция "try-except-else-finally"

try:
	a = int(input("Введите число: "))
	c = 100 / a
	print("Полет нормальный")
except ZeroDivisionError:
	c = 0
	print("Деление на ноль")
except Exception as err:
	print("Исключение: ", err)
# else сработает если нет исключений
else:
	c += 1
	print("Result: ", c)
#  finally срабатывает в любом случае, даже если программа завершается аварийно
finally:
	# внутри должны быть критически важные действия
	# например, закрытие файла или сессии базы данных и т.д.
	print("Сработала finally")

# print("Код после обработки исключений")

# Кастомизированные исключения
# try:
# 	a = int(input("Введите число: "))
# 	if a == 0:
# 		raise Exception('Деление на ноль!')
# 	c = 100 / a
# 	print("Полет нормальный")
# except Exception as e:
# 	print(e)


# **** Пример приближенный к реальности ****

while True:
	try:
		# ввод данных
		a = int(input("Введите число: "))

		# обработка
		c = 100 / a
	except ValueError:
		print("Нужно ввести число!")
		continue
	except ZeroDivisionError:
		print("Вы попытались поделить на ноль!")
		continue
	print("Result: ", c)
	break
