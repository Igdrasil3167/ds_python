# **** Работа с файлами ****

# *** создание файла и запись в этот файл
# контекстный менеджер
# with open("hello.txt", "w") as f:
# 	f.write("hello world\n")
# 	f.write("hello python\n")

# *** перезапись
# with open("hello.txt", "w") as f:
# 	f.write("hello python")


# *** добавление записи
# with open("hello.txt", "a", encoding="utf8") as f:
# 	f.write("Привет мир!\n")


# *** чтение всего файла
with open("hello.txt", encoding="utf8") as f:
	text = f.read()
	print(text)

# чтение отдельных строк
# with open("hello.txt") as f:
# 	text = f.readline()
# 	print(text, end="")
# 	text = f.readline()
# 	print(text, end="")

# чтение строк и создание списка
# with open("hello.txt") as f:
# 	text = f.readlines()
# 	# print(text)
# 	print(text[1])

# удаление строки из файла
# with open("hello.txt", encoding="utf8") as f:
# 	text = f.readlines()
# 	text.remove("altan school\n")
# 	with open("hello.txt", "w", encoding="utf8") as f_2:
# 		for row in text:
# 			f_2.write(row)

