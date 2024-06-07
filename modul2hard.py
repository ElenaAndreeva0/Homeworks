import random
number1 = random.randint(3, 20)
print("Первая вставка", number1)
result = ""
for i in range(1, number1):
    for j in range(i+1, number1 + 1):
        if number1 % (i + j) == 0:
            result += str(i) + str(j)
print(number1, result)