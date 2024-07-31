def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            return f"{result:.3f}"
        else:
            return str(a) + str(b)
    except TypeError:
        return str(a) + str(b)


# def read_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             test = file.read()
#         return test
#     except FileNotFoundError:
#         return "Файл не найден!"
#
#
# def index(number, number_index):
#     try:
#         return number[number_index]
#     except IndexError:
#         return "Индекс за пределами списка"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7), end="\n\n")

# print(read_file('Гусь.png'), end="\n\n")
#
# my_list = [1, 2, 3]
# print(index(my_list, 0))
# print(index(my_list, 3))