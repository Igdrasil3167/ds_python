# *** Кортежи ****

#immutable (Неизменяемый) тип коллекции

my_tuple = (10,20,30)

#Чтение данных из кортежи
num = my_tuple[0]

#Нельзя удалять значения
#del my_tuple[1]

#Нельзя менять значения
#del my_tuple[0] =100

#Длина кортежи
#print( len(my_tuple))


#методы

#метод count(x) возвращает кол-во элементов со значением X
count = my_tuple.count(40)

#метод index(x) возвращает индекс элемента со значением X
idx = my_tuple.index(20)
print(idx)