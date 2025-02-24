""" language = {'name': 'Python', 'version': 3.11}
from datetime import date
my_date = date(2025, 2, 11)
language['start_date'] = my_date
print(language)
 """

""" languages = ["Python", "Java", "C++", "JavaScript"]
for language in languages:
    print(language) """

""" sentence = "The quick brown fox jumps over the lazy dog"
length = 0
for i in sentence:
    if i != " ":
        length = length + 1
print(length) """

""" summary = 0
for i in range(1, 101, 1):
    summary = summary + i
print(summary) """

""" N = 10
sum_squares = 0
i = 1
while i <= N:
    sum_squares = sum_squares + i * i
    i = i + 1
print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}") """

""" def function():
    print('Hello world!') """

""" def print_message(message):
    print(message)
print_message("Це повідомлення з функції.") """

""" message = "Hello world!"
def function(message):
    print(message)
function(message) """

""" N = 10
n = N

def function():
    sum_squares = 0
    i = 1
    while i <= n:
        sum_squares = sum_squares + i * i
        i = i + 1
    return sum_squares


result = function()
print(result) #аргумент функції при виклику """

""" N = 10
def function(n):
    sum_squares = 0
    i = 1
    while i <= n:
        sum_squares = sum_squares + i * i
        i = i + 1
    return sum_squares

result = function(10)
print(result) """

""" first_name = "John"
last_name = "Doe"


def get_fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return(full_name)

fullname = get_fullname(first_name, last_name)
print(fullname) """

""" first_name = "John"
last_name = "Doe"
def get_initials(first_name, last_name):
    initials = last_name + " " + first_name[0] + "."
    return initials
formatted_name = get_initials(first_name, last_name)
print(formatted_name) """

""" first = "Python"
second = "python"


def compare(first, second):
    if first.upper() == second.upper():
        return True
    else:
        return False
result = compare(first, second)
print(result) """

""" text = "Hello, world! Welcome to the world of Python."
world = text.find("world")
position = world

new_text = text.replace("world", "planet")
updated_text = new_text
print(position, updated_text) """

""" product_name = "Coffee Maker"
product_price = 7500.50
product_quantity = 15


def format_product_info(product_name, product_price, product_quantity):
    return f"Product: {product_name}, Price: {product_price} UAH, Quantity: {product_quantity} pcs."
    
product_info = format_product_info(product_name, product_price, product_quantity)
print(product_info) """


""" # Список задач
tasks = [
    "Розробка нової фічі для продукту",
    "Тестування коду",
    "Написання документації",
    "Оптимізація існуючого коду",
    "Робота з клієнтами"
]

# Кількість колег
num_colleagues = 5

# Список для зберігання пріоритетів кожного колеги
priorities = {colleague: [] for colleague in range(1, num_colleagues + 1)}

# Збір відповідей від кожного колеги
for colleague in range(1, num_colleagues + 1):
    print(f"\nКолега {colleague}, встановіть пріоритети для задач (1 - найменший, 5 - найбільший):")
    for task in tasks:
        while True:
            try:
                # Запитуємо пріоритет для кожної задачі
                priority = int(input(f"Встановіть пріоритет для задачі '{task}' (1-5): "))
                if priority < 1 or priority > 5:
                    print("Будь ласка, введіть число від 1 до 5.")
                else:
                    priorities[colleague].append(priority)
                    break
            except ValueError:
                print("Невірний формат! Будь ласка, введіть число від 1 до 5.")

# Тепер ми маємо пріоритети для кожного колеги для кожної задачі

# Обчислюємо, хто на яку задачу буде працювати, вибираючи колегу з найвищим пріоритетом
assigned_tasks = {}

# Перевірка пріоритетів і вибір колеги для кожної задачі
for i, task in enumerate(tasks):
    # Збираємо пріоритети для задачі
    task_priorities = [priorities[colleague][i] for colleague in range(1, num_colleagues + 1)]
    
    # Визначаємо, хто має найвищий пріоритет для цієї задачі
    max_priority = max(task_priorities)
    
    # Шукаємо всіх колег, які мають максимальний пріоритет
    top_colleagues = [colleague for colleague, priority in enumerate(task_priorities, start=1) if priority == max_priority]
    
    # Якщо кілька колег мають однаковий найвищий пріоритет, вибираємо першого з них
    assigned_tasks[task] = top_colleagues[0]

# Перевірка, чи всі колеги отримали задачі
colleagues_with_tasks = set(assigned_tasks.values())
all_colleagues = set(range(1, num_colleagues + 1))

# Якщо є колеги без задач, перерасподіляємо задачі
if colleagues_with_tasks != all_colleagues:
    # Колеги, які не отримали задач
    colleagues_without_tasks = list(all_colleagues - colleagues_with_tasks)
    print(f"\nКолеги без задач: {colleagues_without_tasks}")

    # Перерозподіл задач
    for task, colleague in assigned_tasks.items():
        if colleague in colleagues_without_tasks:
            continue
        # Перерасподіляємо одну з задач
        if colleague == assigned_tasks[task]:
            new_colleague = colleagues_without_tasks[0]  # Призначаємо задачі колезі без задач
            assigned_tasks[task] = new_colleague

# Створення та запис результатів в файл
with open("survey_results.txt", "a") as f:
    f.write("\nРезультати опитування:\n")
    for colleague in range(1, num_colleagues + 1):
        f.write(f"\nРезультати для колеги {colleague}:\n")
        for i, task in enumerate(tasks):
            f.write(f"Задача: {task}\n")
            f.write(f"Пріоритет: {priorities[colleague][i]}\n")
    
    f.write("\nРозподіл задач серед колег:\n")
    for task, colleague in assigned_tasks.items():
        f.write(f"Задача: {task}\n")
        f.write(f"Призначено колезі: Колега {colleague}\n")
    f.write("\n" + "="*40 + "\n")

print("\nРезультати успішно збережені в файл 'survey_results.txt'.")
 """

""" name = input("Як тебе звуть?")
age = input("Скільки тобі років?")
print(f"Привіт, {name}! Тобі {age} років.") """

""" number = int(input('Введіть число'))

if number > 10:
    print("Надто велике число")
elif number < 1:
    print("Замале число")
else:
    for i in range(1, number + 1):
        print(i) """
""" a = 10
b = 5
def function(a, b):
    result = a + b
    return result
res = function(a, b)
print(res) """

""" #Переробити на for i in range(5)
list_of_five = [int(input('Введіть чило1 ')), int(input('Введіть чиcло2 ')), int(input('Введіть чиcло3 ')), int(input('Введіть чиcло4 ')), int(input('Введіть чиcло5 '))]
print(list_of_five)
max_in_list = max(list_of_five)
print('Найбільше число з введених, це', max_in_list) """

""" class Car:
    #Атрибут класу
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        #Атрибут екземпляру
        self.make = make
        self.model = model
        self.year = year
    #Метод екземпляру
    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
#Створення обʼєктів для класу Car
car_ford = Car('Ford', 'Mustang', 2022)
car_toyota = Car('Toyota', 'Corolla', 2021)
print(car_ford.get_info())
print(car_toyota.get_info()) """

""" age = 18
adult1 = age >= 18    # True

age = 15
adult2 = age >= 18    # False
print(adult1)
print(adult2) """

""" var = None
var_int = 10
var_float = 5.5
var_str = 'Рядкове значення'
var_bool = True """

""" first_name = 'Andrii'
last_name = 'Derenhovskyi'
full_name = first_name + ' ' + last_name
print(full_name) """

""" some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]
some_iterable[1] = "d"
print(some_iterable)  # ["a", "d", "c"] """

""" data = [1, 3.11]
some_data = ['python']
data.extend(some_data)
data.insert(1, 'python')
data.reverse()
print(data) """

""" data = {}
data['order'] = 1
data['lang'] = 'python'
data['version'] = 3.11
print(data) """

""" data = {}
info = {"status": "student", "school": "GoIT"}
data["name"] = "Andrii"
data["age"] = 29
data["hobbies"] = ["running", "cycling"]
age = data.get("age")
data.update(info)
print(age)
print(data) """

# print("Привіт", end=" ")

# # Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# # Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# # Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant + \
#              num_glasses * price_per_glass + \
#              num_coffee_packs * price_per_coffee_pack

# # Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# # Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")

# print("The \'Tom's phone\' article")   # Екранування для лапок '' і апострофа '

# item_one = 34.34  
# item_two = 12.01
# item_three = 17.42
# item_four = 4.93

# bill = item_one + item_two + item_three + item_four

# print(f'Ваш рахунок складає:', f'{int(bill)} доларів', f'{int((bill - int(bill)) * 100)} центів', sep='\n')

""" FLOORS = 5
APARTMENT_PER_FLOOR = 4

apartment_number = int(input('Enter apartment number: '))

apartment_in_entrance = FLOORS * APARTMENT_PER_FLOOR

entrance_number = (apartment_number - 1) // apartment_in_entrance + 1

floor_number = ((apartment_number - 1) % apartment_in_entrance) // APARTMENT_PER_FLOOR + 1

print(f'Entrance number is: {entrance_number}', f'Floor is: {floor_number}', sep='\n') 
 """
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))  # {3}
# print(a & b)  # {3}

# name = 'Andrii'
# age = 29
# is_active = False
# subscription = None
# print(type(name), type(age), type(is_active), type(subscription), sep='\n')

# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active = bool(input("Do you want to receive a message? "))
# print((name), (email), (age), (height), (is_active))
# print(type(name), type(email), type(age), type(height), type(is_active))

# data = {}
# data['year'] = 2024
# data['lang'] = 'Python'
# data['version'] = 3.12


# print(data)
# print(type(data))

# cat = {}
# info = {"status": "vaccinated", "breed": True}

# cat['nick'] = 'Simon'
# cat['age'] = 7
# cat['characteristics'] = ["лагідний", "кусається"]
# age = cat.get('age')
# cat.update(info)
# print(cat)

# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else: 
#     is_next = False
# print(is_next)

# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")

# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience <= 1:
#     developer_type = "Junior"
# elif work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# else:
#     developer_type = "Senior"
# print(developer_type)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 != 0:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)

#Є список із числами numbers. Напишіть цикл for для знаходження суми елементів списку чисел numbers, 
# які діляться на 3 без залишку. 
# Початковий список numbers змінювати не можна.
# Результат треба присвоїти змінній sum_num.

# numbers = [10, 4, 201, 21, 12, 2, 132, 7, 1, 18, 3, 12, 6, 15, 4, 27]
# sum_num = 0

# for i in numbers:
#     if i % 3 == 0:
#         sum_num = sum_num + i
# print(sum_num)


# N = 10
# def function(n):
#     sum_squares = 0
#     i = 1
#     while i <= n:
#         sum_squares = sum_squares + i * i
#         i = i + 1
#     return sum_squares

# result = function(10)
# print(result)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# i = 0
# while i <= num:
#     sum = sum + i
#     i = i + 1
# print(sum)

# first = "Python"
# second = "python"
# def compare(first, second):
#     if first.upper() == second.upper():
#         return True
#     else:
#         return False
# result = compare(first, second)
# print(result)

# def invite_to_event(username):
#     return print(f"Dear {username}, we have the honour to invite you to our event")

# invite_to_event('Stepan')

# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# x = int(input('Введіть координату х: '))
# y = int(input('Введіть координату y: '))

# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# is_nice = True
# if is_nice:
#     state = "nice"
# else:
#     state = "not nice"
# print(state)

# pets = ["dog", "fish", "cat"]
# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")

# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

# def is_even(num: int) -> bool:
#     return num % 2 == 0
    
# check_even = is_even(0)
# print(check_even)  # Виведе: True

# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)

# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)

# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)
# func((1, 2, 3), 4, 5)

# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ' + ' ', 5)

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

example_1 = "1 2 3 4 5"
example_2 = "1 2 -3 4 5"
example_3 = "1 9 3 4 -5"
def higt_and_low(numbers_str: str) -> str:
    numbers = numbers_str.split()
    numbers.sort()
#    higt = numbers.pop(0)
#    low = numbers.pop(-1)
    return print(numbers.pop(0), numbers.pop(-1))
higt_and_low(example_3)