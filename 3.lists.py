# **** Списки (lists) ****


# создание пустого списка

my_list = []
my_list_2 = list()

# метод списков append, который добавляет объект в конец списка

my_list_2.append(100)
my_list_2.append(100)
my_list_2.append(777)

my_list_2.append("hello")

my_list_2.append([1,2,3])

# обращение к элементам списка

el = my_list_2[0] # извлечение значения по индексу

# del my_list_2[1] # удаление элемента по индексу

my_list_2[1] = 200 # замена значения


# создание заполненного списка

my_list = [10,20,30,40,"A","B"]

s = "привет, Мир!"
my_list_3 = list(s)


# *** функция range() ***

# range(end), создается набор чисел от 0 до числа end (не включительно)
# range(start, end), создается набор чисел от start до числа end (не включительно)
# range(start, end, step), создается набор чисел от start до числа end (не включительно) с шагом step

numbers = list(range(5))
numbers = list(range(1, 5))
numbers = list(range(1, 10, 2))
numbers = list(range(10, 1, -1))


# *** методы списка ***

a = [10,20,30,40,50]

# append - метод добавления элемента

# объект.метод()
a.append(100)

# insert - добавляет элемент по индексу
a.insert(0, 7)

# remove - удаляет элемент по значению
a.remove(30)

# clear - очистка списка
# print(a)
# a.clear()

# sort - сортировка списка
b = [8,2,1,7,3,2,8,4,1]
b.sort(reverse=True)

# reverse - поворот списка
c = [1,2,3]
c.reverse()

# pop()
# count()
# index()

print(c)