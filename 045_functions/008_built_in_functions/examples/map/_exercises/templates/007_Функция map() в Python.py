#В Python функция map принимает два аргумента: функцию и аргумент составного типа данных, например, список.
# map применяет к каждому элементу списка переданную функцию. Например, вы прочитали из файла список чисел,
# изначально все эти числа имеют строковый тип данных, чтобы работать с ними - нужно превратить их в целое число:

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = []
for item in old_list:
new_list.append(int(item))
print (new_list)
# [1, 2, 3, 4, 5, 6, 7]

# Тот же эффект мы можем получить, применив функцию map:

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print (new_list)

# [1, 2, 3, 4, 5, 6, 7]

# Как видите такой способ занимает меньше строк, более читабелен и выполняется быстрее. map также работает и
# с функциями созданными пользователем:

def miles_to_kilometers(num_miles):
    return num_miles * 1.6

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print (kilometer_distances)
# [1.6, 10.4, 27.84, 3.84, 14.4]

# А теперь то же самое, только используя lambda выражение:

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

print (kilometer_distances)
# [1.6, 10.4, 27.84, 3.84, 14.4]

# Функция map может быть так же применена для нескольких списков, в таком случае функция-аргумент должна принимать
# количество аргументов, соответствующее количеству списков:

l1 = [1,2,3]
l2 = [4,5,6]

new_list = list(map(lambda x,y: x + y, l1, l2))
print (new_list)
# [5, 7, 9]

# Если же количество элементов в списках совпадать не будет, то выполнение закончится на минимальном списке:

l1 = [1,2,3]
l2 = [4,5]

new_list = list(map(lambda x,y: + y, l1, l2))

print (new_list)
# [5,7]

# Функция filter() в Python: