def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params()

def print_params(a=1, b="строка", c=True):
    print(a, b)


print_params()

def print_params(a=1, b="строка", c=True):
    print()


print_params()

def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params(b= 25)

def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params(c= [1, 2, 3])


def print_params(a, b, c):
    print(a, b, c)


value_list_=[5, "tree", True]
print_params(*value_list_)

def print_params(**values_dict):
    for key, value in values_dict.items():
        print(key, value)


values_dict= {"a": 3, "b": "cow", "c": True}
print_params(**values_dict)

def print_params(a=1, b="строка", c=True):
    print(a, b, c)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

