# *** Генератор пароли ***

import hashlib
from tkinter import Tk, StringVar, Label, Entry, Button

def hashing():
	"""
	Функция шифрования
	"""
	# строка пароли
	origin_str = pwd.get()
	# кодировние
	byte_str = origin_str.encode()
	# шифрование
	hash_str = hashlib.sha256(byte_str)
	# преобразование в строку hex-числа
	hex_str = hash_str.hexdigest()[:10]
	# передаем в переменную pwd_hash
	pwd_hash.set(hex_str)
	# запись в файл
	with open('pwd.txt', "w") as f:
		f.write(f"{pwd.get()} : {pwd_hash.get()}")

# объект окна
window = Tk()
# заголовок окна
window.title("Password generator")

# переменные с объектами класса StringVar
pwd = StringVar()
pwd_hash = StringVar()

# Текстовая метка созданная компонентом (виджетом, элементом) Label
# Label позволяет выводить статический текст без возможности редактирования
label = Label(text="Пароль:")
# Позиционирование методом grid (сетка)
label.grid(row=0, column=0, padx=5, pady=5)

# Поле ввода/вывода текста осуществляется виджетом Entry
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)

# Создание кнопки
Button(text="Click me", command=hashing).grid(row=1, column=0, padx=5, pady=5)

# Вывод текста
Entry(textvariable=pwd_hash).grid(row=1, column=1, padx=5, pady=5)

# запуск основного цикла
window.mainloop()