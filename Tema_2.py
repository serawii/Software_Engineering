from datetime import datetime 
print(datetime.now()) #Выводит текущую дату и время

# lab1
print(123)
print("123")
print(123.2)

# lab2
print(51025105210 - 512521)
print(551.1 + 53912.2)
print(3 + 512.521 + 5 + 21.98)

# lab3
print("hello")

world = "world"
print(f"hello {world}")

one = "hello"
two = "world"
print(one + two)

# lab4
first = "hello"
print(bool(first))

second = 142
print(float(second))

third = None
print(str(third))

# lab5
one = input("one: ")
two = input("two: ")
three = input("three: ")
print(one, two, three)

# lab6
a = 60
b = 6
print("Возведение в степень:", a ** b)
print("Обычное деление: ", a / b)
print("Целочисленное деление:", a // b)
print("Нахождение остатка от деления:", a % b)

# lab7
line = "world"
print(line * 6)

# lab8
sentence = "Hello World"
print(sentence.count("o"))

# lab9
print("Hello\nWorld")

# lab10
sentence = "Hello World"
print(sentence[1])
print(sentence[:5])

# 1
print(bool(0))

# 2
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# 3
num = int(input("num = "))
print(num)

# 4
st = "HELLO WORLD!"[:5]
print(st * (int(16 / len(st)) + 1))

# 5
day, month, year = 26, "сентября", 2023
print(f"Сегодня {day} {month} {year}.", end=" Всего хорошего!\n")

# 6
st = "Hello World"
print(st.replace(" ", " my "))

# 7
print(len("Hello World"))

# 8
print("HELLO WORLD".lower())

# 9
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b ** 2 - 4 * a * c
print(f"D = {D}")

# 10
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
print(f"{name.title()} {surname.title()}, ", end="вы успешно авторизированы в системе!\n")