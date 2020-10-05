# *** Множество (set) ***

# особенности:
# - неупорядоченным типом коллекции (объекты не индексируются)
# - при создании автоматически удаляет дублирующие объекты


# *** создание наполненного множества ***

# первый способ
my_set = {"a", "c", "b"}

# второй способ
s = "hello"
l = [10,20,30,30]

my_set_2 = set(l)


# *** добавление элемента ***

my_set.add(100)


# *** удаление элемента ***

# my_set.remove("a")

# *** проблема при удалении ***

# my_set.remove("d")

# решение проблемы

# if "d" in my_set:
# 	my_set.remove("d")
# else:
# 	print("такого значения нет внутри множества")

# метод, удаляющий элемент без ошибок
# my_set.discard("a")


# *** объединение множеств ***

users = {"John", "Tom", "Andrey"}

new_users = {"John", "Kate", "Bob"}

# users = users.union(new_users)
# users.update(new_users)

# короткий аналог метода union()
union_users = users | new_users

# *** пересечение ***

intersect_users = users.intersection(new_users)

# короткий аналог метода intersection()
intersect_users = users & new_users


# *** разность ***

# diff_users = users.difference(new_users)

# sd_users = users.symmetric_difference(new_users)

# короткий аналог метода difference()
diff_users = users - new_users

print(union_users)