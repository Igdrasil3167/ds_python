# *** Основы объектно-ориентированного программирования (ООП) ***

# Объекты обладают свойствами и методами
# Каждый объект должен принадлежать определенному классу (типу)
# Класс - это "чертеж" объекта
# конкретный реализованный на базе класса объект называется экземпляром класса


# создание класса. Название принято писать с заглавной буквы
class Cat:
	# метод-конструктор
	def __init__(self):
		# свойства (атрибуты, поля)
		self.name = None

	# метод - функция, принадлежащая классу
	def mur(self):
		return self.name

# создание объекта на базе класса Cat (т.е. экземпляра класса Cat)
cat_1 = Cat()

# чтение свойства
var = cat_1.name
# print("Значение var ДО изменения: ", var)

# запись в свойство
cat_1.name = 100
# print(cat_1.name)
# print("Значение var ПОСЛЕ изменения: ", var)

# var = 10
# print(cat_1.name)

# вызов метода экземпляра
res = cat_1.mur()
# print("Результат: ", res)

# каждый объект (экземпляр класса) независим
# создание 2-го экземпляра класса Cat
cat_2 = Cat()
cat_2.name = 200

# вызов метода обеих объектов
# print(cat_1.mur())
# print(cat_2.mur())


# *** Принцип Наследования - принцип ООП ***

# создание родительского (предкового) класса
class Animal:
	def __init__(self):
		self.num_legs = 0

# создание дочерних классов
class Dog(Animal):
	def __init__(self, name):
		self.name = name

	def info(self):
		print(f"My name is {self.name}. Legs: {self.num_legs}")
	
class Insect(Animal):
	"""
	docstring
	"""
	def __init__(self, name):
		self.name = name

	def info(self):
		print(f"My name is {self.name}. Legs: {self.num_legs}")

# создание экземпляров дочерних классов
dog_1 = Dog("Мурзик")
dog_1.num_legs = 4

bug = Insect('Bug')
bug.num_legs = 8

# вызов метода дочерних классов
# dog_1.info()
# bug.info()

class Human(object):
	"""
	docstring
	"""
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def info(self):
		print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}")

class Pilot(Human):
	def skill(self):
		print("я умею летать")

class Medic(Human):
	def skill(self):
		print("я умею лечить")

	def therapy(self, obj):
		print(f"Я вылечил {obj.name}")

class Simple_human(Human):
	pass

john = Pilot("John", 45, 82.4)
katrin = Medic("Katrin", 35, 67.5)
petya = Simple_human("Petya", 5, 23.1)

# вызов метода общего для всех (метод наследуется от родительского класса)
john.info()
katrin.info()
petya.info()

# вызов метода, которым обладают все классы, кроме класса Simple_human
john.skill()
katrin.skill()

# вызов метода, которым обладает только класс Medic
katrin.therapy(john)

# try:
# 	petya.skill()
# except AttributeError:
# 	print("у него нету метода skill")
# 	petya.info()


# **** Полиморфизм ****
# поли + морф = разные формы чего-то одного

# 1 вид полиморфизма - методы у разных классов переопределяются,
# т.е. методы имеют одинаковое название, но могут иметь различное поведение

# родительский класс
class A:
    """
    docstring
    """
    def funk (self, arg):
        """
        docstring
        """
        res = arg * 2
        print(f"Данные: {res}")

# Дочерний класс у которого метод переопределен
class A_1(A):
    """
    docstring
    """
    def funk (self, arg):
        res = arg ** 3
        print(f"Result: {res}")

# Экземпляры классов
a = A()
a_1 = A_1()

# 
a.funk(10)
a_1.funk(10)

# 2 вид полиморфизма - применение "Магические" методы (методы перегрузки операторов)

# метод, который делает из экземпляра класса функцию
class Sum(object):
    """
    docstring
    """
    def __init__(self, param):
        self.coeff = param

    def __call__(self, a, b):
        res = (a + b) * self.coeff
        print(f"Result: {res}")

    def __str__(self):
        return f"Sum {self.coeff}" 

s_1 = Sum(0.5)
s_2 = Sum(3.14)

# Объект ведет себя как функция 
# s_1(10, 20)
# s_2(10, 20)

# Объект при передаче в функцию print возвращет строку
# print(s_1)


# **** Инкопсуляция ****
# Инкапуляция 

# Инкопсуляциb не строгая 
class B:
    def __init__(self, arg):
        self._attr = arg

    def _method(self):
        print("Hello!")

b = B(100)

# print(b._attr)
# b._method()

# Инкопсуляция строгая 
class C:
    def __init__(self, arg):
        self.__attr = arg

    def method_2(self):
        return self.__attr

    def __method(self):
        print("Hello!")

c = C(200)
c._C__method()
# print(c._C__method())

# **** Композиция (Агрегация) ****
# Использование экземпляров одного класса внутри другого

class D:
    def __call__(self, a):
        return a ** 2

class E:
    def m(self, b):
        d = D() #создается объект класса D
        res = b + 2
        return d(res) # Используется объект класса D в качестве функции 

e = E()
res = e.m(10)
print(res)


# Статический метод, метод класса 

class Person:
    # Статическая переменная 
    counter = 0
    def __init__(self, name, age):
        self.__n = name
        self.__a = age
        Person.counter += 1
        self.id = Person.counter

    # Метод экземпляра
    def info(self):
        print(f"Id: {self.id}, Name: {self.__n},Age: {self.__a}")

    # Метод класса
    @classmethod
    def count_counter(cls):
        cls.counter += 1

    # Статический метод
    @staticmethod
    def method (x, y):
        print(f"Res: {x + y}")

john = Person("John", 20)
john.info()
# john.count_control()

bob = Person('Bob', 35)
bob.info()

bob.method(10,20)
Person.method(10,20)
