from datetime import datetime
print(datetime.now()) #Выводит текущую дату и время

#Lab_rabota
# 1
one = int(input("Введите значение первой переменной: "))
two = int(input("Введите значение второй переменной: "))
if one > two:
    print("Выполняется")
else:
    print("Не выполняется")

# 2
one = int(input("Введите значение переменной: "))
if one < 0:
    print("Переменная меньше 0")
elif 0 < one < 10:
    print("Переменная больше 0 и меньше 10")
else:
    print("Переменная больше 10")

# 3a
numbers = [1, 3, 4, 6, 8, 9]
value = int(input("Введите значение переменной: "))
if value in numbers:
    print("Переменная есть в данном массиве")
else:
    print("Переменной нет в этом массиве")

# 4
numbers = [1, 3, 4, 6, 8, 9, 15, 16, 73, 321, 322]
value = int(input("Введите значение переменной: "))
if value in numbers:
    if value % 2 == 0:
        print("Переменная четная и есть в массиве numbers")
    else:
        print("Переменная нечетная и есть в массиве numbers")
else:
    print(f"Переменной нет в массиве numbers и она равна {value}")

# 5
for i in range(10):
    print("i =", i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print("Переменная равна 2 или 3")
    elif i in [4, 5, 6]:
        print("Переменная равна 4, 5 или 6")
    else:
        break

# 6
string = "Привет всем изучающим Python!"
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")

# 7
value = 100
for i in range(10, -1, -1):
    value -= i
    print(i, value)

# 8
value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5
    print(value)

# 9
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass
print(value)

# 10
even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True
if flag is True:
    print("В массиве есть нечетное число")
else:
    print("В массиве есть числа четные")

#Sam_rabota
from datetime import datetime
print(datetime.now())

# 1
num = 1
for i in range(2):
    num *= 5
    num += 1
print(num)

# 2
st = "Hello World"
for i in range(len(st)):
    print(st[-(i + 1)])

# 3
number = int(input("number = "))
if number < 0 or number > 10:
    print("Число должно быть от 1 до 10!")
else:
    if 0 <= number <= 3:
        print("Число от 0 до 3 включительно")
    elif 3 < number < 6:
        print("Число от 3 до 6")
    elif 6 <= number <= 10:
        print("Число от 6 до 10 включительно")

# 4
sentence = input("Введите строку: ")
print("Длина:", len(sentence))
print("Нижний регистр:", sentence.lower())
print("Гласных:", sum(1 for letter in sentence if letter in ['a', 'e', 'i', 'o', 'u']))
print("Замененная строка:", sentence.replace("ugly", "beauty"))
print("Строка начинается со 'The':", sentence.startswith("The"))
print("Строка начинается со 'end':", sentence.endswith("end"))

# 5
string = "hello"
values = [0, 2, 4, 6, 8, 10]
counter = 0
while ' world' not in string:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    if counter < 10:
        string = memory
    counter += 1
