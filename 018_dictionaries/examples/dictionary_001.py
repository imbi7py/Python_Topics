# Создать Словарь
# diсt(<Ключ1>=<Значение1>[, ... , <КлючN>=<ЗначениеN>])

d = dict({"a": 1, "b": 2})
print(d)
# {'a': 1, 'b': 2}

# Создать  Список кортежей
d = dict([("a", 1), ("b", 2)])
print(d)
# {'a': 1, 'b': 2}

# Создать Список списков
d = dict([["a", 1], ["b", 2]]); print(d)
# {'a': 1, 'b': 2}

# Объединить два списка в список кортежей позволяет функция zip()
k = ["a", "b"] # Список с ключами
v = [1, 2]  # Список со значениями
print(list(zip(k, v))) # Создание списка кортежей
# [('a', 1), ('b', 2)]
d = dict(zip(k, v)); print(d)# Создание словаря
# {'a': 1, 'b': 2}

# указав все элементы словаря внутри фигурных скобок. Это наиболее часто используемый
# способ создания словаря. Между ключом и значением указывается двоеточие, а пары
# «Ключ!значение» записываются через запятую.
d = {}; print(d)   # Создание пустого словаря
# {}
d = { "a": 1, "b": 2 }; print(d)
# {'a': 1, 'b': 2}

# заполнив словарь поэлементно
d = {} # Создаем пустой словарь
d["a"] = 1# Добавляем элемент1 (ключ "a")
d["b"] = 2 # Добавляем элемент2 (ключ "b")
print(d)
# {'a': 1, 'b': 2}

# dict. fromkeys ( <Последовательность> [, <Значение>])

# Метод создает
# новый словарь, ключами которого будут элементы последовательности, переданной
# первым параметром, а их значениями - величина, переданная вторым параметром. Если второй параметр не указан,
# то значением элементов словаря будет значение None.

d = dict.fromkeys(["a", "b", "c"])
print(d)
# {'a': None, 'c': None, 'b': None}
d = dict.fromkeys(["a", "b", "c"], 0)     # Указан список
print(d)
# {'a': 0, 'c': 0, 'b': 0}
d = dict.fromkeys(("a", "b", "c"), 0)     # Указан кортеж
print(d)
# {'a': 0, 'c': 0, 'b': 0}

# При создании словаря в переменной сохраняется ссылка на объект, а не сам объект.
# Это обязательно следует учитывать при групповом присваивании. Групповое присваивание можно испо льзовать для чисел и
# строк, но для списков и сло варей этого делать нельзя.
d1 = d2 = {"a": 1, "b": 2} # Якобы создали два объекта
d2["b"] = 10
print(d1, d2) # Изменилось значение в двух переменных !!!
# ({'a': 1, 'b': 10}, {'a': 1, 'b': 10})

# Как видно из примера, изменение значения в переменной d2 привело также к изменению
# значения в переменной d1. То есть, обе переменные ссылаются на один и тот же объект, а не на два разных объекта.

# Чтобы получить два объекта, необходимо производить раздельное
# присваивание:
d1, d2 = {"a": 1, "b": 2}, {"a": 1, "b": 2}
d2["b"] = 10
print(d1, d2)
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 10})

# Creating a shallow copy of the dictionary using the dict () function
d1 = {"a": 1, "b": 2} # Создаем словарь
d2 = dict(d1) # Создаем поверхностную копию
print(d1 is d2)# Оператор показывает, что это разные объекты
# False
d2["b"] = 10
print(d1, d2)  # Изменилось только значение в переменной d2
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 10})

# Creating a shallow copy of the dictionary using the copy () method
d1 = {"a": 1, "b": 2} # Создаем словарь
d2 = d1.copy()# Создаем поверхностную копию
d1 is d2  # Оператор показывает, что это разные объекты
# False
d2["b"] = 10
print(d1, d2)# Изменилось только значение в переменной d2
# ({'a': 1, 'b': 2}, {'a': 1, 'b': 10})

# Creating a complete copy of the dictionary
d1 = {"a": 1, "b": [20, 30, 40]}
d2 = dict(d1)# Создаем поверхностную копию
d2["b"][0] = "test"
d1, d2 # Изменились значения в двух переменных!!!
# ({'a': 1, 'b': ['test', 30, 40]}, {'a': 1, 'b': ['test', 30, 40]})
import copy
d3 = copy.deepcopy(d1) # Создаем полную копию
d3["b"][1] = 800
d1, d3 # Изменилось значение только в переменной d3
# ({'a': 1, 'b': ['test', 30, 40]}, {'a': 1, 'b': ['test', 800, 40]})

# Обращение к элементам словаря
# осуществляется с помощью квадратных скобок, в которых
# указывается ключ. В качестве ключа можно указать неизменяемый объект - например:
# число, строку или кортеж.

# Выведем все элементы словаря:
d = {1: "int", "a": "str", (1, 2): "tuple"}
print(d[1], d["a"], d[(1, 2)])
# ('int', 'str', 'tuple')

# Если элемент, соответствующий указанному ключу, отсутствует в словаре, то возбуждается
# исключение KeyError:
d = {"a": 1, "b": 2}
# d["c"] # Обращение к несуществующему элементу