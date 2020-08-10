# -*- coding: utf-8 -*-

"""Пример открытия файла для чтения"""

def read_file(fname):
	"""Функция для чтения файла fname
	и вывода его содержимого на экран
	"""

	# Открытие файла для чтения
	file = open(fname, 'r')

	# Вывод названия файла
	print('File ' + fname + ':')
    # Чтение содержимого файла построчно
	for line in file:
		# Вывод строки s.  Перевод строки в файле сохраняется в строке, поэтому
		# выводим без дополнительного перевода строки.
		print(line, end='')

	# Закрытие файла
	file.close()


if __name__ == '__main__':
    read_file('data/file.txt')
