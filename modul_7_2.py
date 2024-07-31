def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for string in strings:
        byte = file.tell()
        file.write(string + '\n')
        strings_positions[(len(strings_positions) + 1, byte)] = string
    return strings_positions
    file.close()



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('../test.txt', info)
for elem in result.items():
    print(elem)


'''Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.

Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
'''

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    for i, s in enumerate(strings):
        key = (i+1, file.tell())
        strings_positions[key] = s
        file.write(s + '\n')
    file.close()
    return strings_positions

def main():
    # Пример результата выполнения программы:
    # Пример выполняемого кода:
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('../test.txt', info)
    for elem in result.items():
        print(elem)

if __name__ == '__main__':
    main()

'''
Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')'''

