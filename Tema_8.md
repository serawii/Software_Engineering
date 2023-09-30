# Тема 7. Введение в ООП
Отчет по Теме #7 выполнил(а):
- Багаева Полина Сергеевна
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.
## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Polina", 21)
print(person1.introduce())
```
### Результат.
![Меню](https://github.com/serawii/Software_Engineering/blob/Тема_8/pic/сам1.png)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(person1.introduce())`: Выводит имя и возраст.
  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"{self.name} added {friend.name} as a friend.")
```
### Результат.
![Меню](https://github.com/serawii/Software_Engineering/blob/Тема_7/pic/сам2.png)

## Выводы

В данном коде выводятся четыре строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print("\nВыберите действие:")`: Выводит возможные варианты для выбора действия.

2. `print("1. Ввести новый расход")`: Вводит новый расход.

3. `print("2. Показать все расходы")`: Показывает все введеные расходы.

4. `print("3. Выйти")`: Выходит из программы.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
with open('.\\input (1).txt', 'r') as file:
    text = file.read()

letter_count = len([char for char in text if char.isalpha()])
word_count = len(text.split())
line_count = text.count('\n') + 1  # добавляем 1, так как последняя строка не завершается символом новой строки

print("Input file contains:")
print(f"{letter_count} letters")
print(f"{word_count} words")
print(f"{line_count} lines")
```
### Результат.
![Меню](https://github.com/serawii/Software_Engineering/blob/Тема_7/pic/сам3.png)

## Выводы

В данном коде выводятся четыре строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print("Input file contains:")`: Выводит статистику файла.

2. `print(f"{letter_count} letters")`: Выводит количество букв.

3. `print(f"{word_count} words")`: Выводит количество слов.

4. `print(f"{line_count} lines")`: Выводит количество строк.
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, 

```python
import re


def load_prohibited_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words


def multiple_replace(target_str, bad_words):
    for word in bad_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        target_str = pattern.sub("*" * len(word), target_str)
    return target_str


if __name__ == "__main__":
    output_sentence = multiple_replace(input("Enter a sentence: "), load_prohibited_words(".\\input (2).txt"))
    print(f"Modified sentence:\n{output_sentence}")
```
### Результат.
![Меню](https://github.com/serawii/Software_Engineering/blob/Тема_7/pic/сам4.png)

## Выводы

В данном коде выводится одна строка с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(f"Modified sentence:\n{output_sentence}")`: Выводит измененный текст, учитывая запрещенные слова.
  
## Самостоятельная работа №5
### Анализ текстовых данных: поиск наиболее часто встречающихся слов и фраз в большом текстовом файле.

```python
from collections import Counter
import re


if __name__ == "__main__":
    with open(".\\large_text.txt", "r", encoding="utf-8") as file:
        text = file.read()
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)

        word_counts = Counter(words)
        most_common_words = word_counts.most_common(10)

        phrases = re.findall(r'\b\w+\s\w+\b', text)
        phrase_counts = Counter(phrases)
        most_common_phrases = phrase_counts.most_common(10)

    print("Наиболее часто встречающиеся слова:")
    for word, count in most_common_words:
        print(f"{word}: {count} раз")

    print("\nНаиболее часто встречающиеся фразы:")
    for phrase, count in most_common_phrases:
        print(f"{phrase}: {count} раз")
```
### Результат.
![Меню](https://github.com/serawii/Software_Engineering/blob/Тема_7/pic/сам5.png)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(f"{word}: {count} раз")`: Выводит часто встречающиеся слова.

2. `print(f"{phrase}: {count} раз")`: Выводит часто встречающиеся фразы.