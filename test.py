# example_1 = "1 2 3 4 5"
# example_2 = "1 2 -3 4 5"
# example_3 = "1 9 3 4 -5"
""" def high_and_low(numbers_str: str) -> str:
    numbers = numbers_str.split()
    int_list = list(map(int, numbers))
    int_list.sort()
    return f'{int_list.pop(-1)} {int_list.pop(0)}'
high_and_low('456 234 -567 345 341 -100 -1 1 6') """

# def high_and_low(numbers_str: str) -> str:
#     numbers = list(map(int, numbers_str.split()))
#     return f"{max(numbers)} {min(numbers)}"

""" 
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
 """

# def solution(string):
#     return string[::-1]
# print(solution('world'))

""" 
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]
 """

# def digitize(n):
#     n_str = str(n)  
#     digits_list = [int(digit) for digit in n_str]
#     reversed_list = digits_list[::-1]
#     return reversed_list

""" 
Create a function that accepts a parameter representing a name and returns the message:
 "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
 """

# def greet(name):
#     return f'Hello, {name} how are you doing today?'
# print(greet('Andrii'))

# def greet(name):
#     return "Hello, {} how are you doing today?".format(name)

# def greet(name):
#     return "Hello, " + name + " how are you doing today?"

# def greet(name):
#     return "Hello, %s how are you doing today?" % name

""" 
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
 """

# def abbrev_name(name: str) -> str:
#     full_name = name.split()
#     name_1 = full_name[0].capitalize()
#     name_2 = full_name[1].capitalize()
#     return name_1[0] + '.' + name_2[0]

# age = int(input('How old are you? '))
# def adult(age: int) -> str:
#     return f'Adult is {True if age >= 18 else False}'
# print(adult(age))

""" 
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
 """

# def grow(arr):
#     sum_num = 1
#     for i in arr:
#         sum_num *= i
#     return sum_num 

# import math
# def grow(arr):
#     return math.prod(arr)

# print(grow([1.4, 2.4, 3, 4]))

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# words = []
# start = 0

# for indx, char in enumerate(text):
#     if not char.lower() in alphabet:
#         word = text[start:indx]
#         words.append(word.strip())
#         start = indx

# for indx, char in enumerate(text):
#     if not char.lower() in alphabet:
#         word = text[start:indx]
#         if word.strip():
#             words.append(word.strip())  # Додаємо слово без пробілів
#         start = indx + 1  # Починаємо нове слово після розділового знака

# # Додаємо останнє слово, якщо воно є
# if start < len(text):
#     words.append(text[start:].strip())

# print(words)

# def email_slice():
#     mail = input('Input your email address: ')
#     mail_at = mail.index('@')
#     user_name = mail[:mail_at]
#     domain_name = mail[mail_at+1::]
#     return print(f'For {mail} \nyour user name: {user_name} \nyour domain: {domain_name}')
# email_slice()

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool / quantity
#     chunk = round(chunk)
#     print(chunk)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price, discount
#         price = price * (1 - discount)
#         return price
#     apply_discount()
#     return price
# print(discount_price(40, 0.05))

# def get_fullname(first_name, last_name, middle_name=''):
#     if middle_name == '':
#         name = f"{first_name} {last_name}"
#     else:
#         name = f'{first_name} {middle_name} {last_name}'
#     return name
# print(get_fullname('firstname', 'lastname', 'middlename'))

# def format_string(string: str, length: int) -> str:
#     if len(string) >= length:
#         new_string = string
#     else:
#         space_left = (length - len(string)) // 2
#         space_right = (length - len(string)) - space_left
#         new_string = " " * space_left + string + space_right * " "
#     return new_string
# print(format_string('aaaaaaaaaaaaaaaaac', 12))

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def number_of_groups(n, k):
#     sum_num_list = factorial(n) / ((factorial(n - k) * factorial(k)))
#     return int(sum_num_list)
# print(number_of_groups(50, 7))

# from random import randint # Імпортуємо функцію, для генерування числа

# def predict_number(number): # створюємо функцію, яка приймає число на вхід для діапазону чисел
#     count = 0 # лічильник для спроб вгадування числа
#     goal = randint(0, number) # генеруємо число від 0 до аргументу функції

#     while True: # вічний
#         user_input = int(input(f"Guess the number form 0 to {number}: ")) # користувач вводить число з підказкою у вигляді діапазону
#         count += 1 # При кожному ведені лічилдьник збільшується на один

#         if user_input > goal: # Якщо число введегне є більше за генероване повідомляємо користувача
#             print("Smaller")
#         elif user_input < goal: #  Якщо число введегне є менше за генероване повідомляємо користувача
#             print("Larger")
#         else: #  Якщо число введегне рівне генерованому повідомляємо користувача і перериваємо цикл
#             print(f"You win! Number of attempts {count}")
#             break

# predict_number(10)


# def fibonachi_iter(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(fibonachi_iter(101))  # Виведе 573147844013817084101

# def revers_seq(n: int) -> list:
#     my_list = []
#     while n >= 1:
#         my_list.append(n)
#         n = n -1
#     return my_list
# print(backward_count(5))

# def backward_count(n: int) -> list:
#     return list(range(n, 0, -1))

# def square_every_digit(num: int) -> int:
#     str_num = str(num)
#     sentences = ''
#     for i in str_num:
#         n = int(i) ** 2
#         sentences += str(n)
#     return int(sentences)
# print(square_every_digit(9119))
# print(type(square_every_digit(9119)))

# def square_every_digit(num: int) -> int:
#     return int("".join(str(int(digit) ** 2) for digit in str(num)))

""" 
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -- every time you press the button 
it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block for each letter (direction) and you know it takes you one minute 
to traverse one city block, so create a function that will return true if the walk the app gives you will take you 
exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. 
Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters 
('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
 """
# def ten_min_walk(walk: list) -> bool:
#     if len(walk) != 10:
#         return False
#     north_south = walk.count('n') - walk.count('s')  # Має бути 0
#     east_west = walk.count('e') - walk.count('w')    # Має бути 0

#     return north_south == 0 and east_west == 0
# print(ten_min_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True
# print(ten_min_walk(['n', 'n', 'n', 's', 's', 's', 'e', 'w', 'e', 'w']))  # True
# print(ten_min_walk(['n', 's', 'n', 's']))  # False (тільки 4 кроки)
# print(ten_min_walk(['n', 'n', 'n', 'n', 's', 's', 's', 's', 'e', 'w']))  # False

# def isValidWalk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# def check(x_o: list) -> bool:
#     count_x = 0
#     count_o = 0
#     for char in x_o:
#         if char == 'x':
#             count_x += 1
#         elif char == 'o':
#             count_o += 1
#         elif char == 'X':
#             count_x += 1
#         elif char == 'O':
#             count_o += 1
#     return count_x == count_o

# def xo(x_o: list) -> bool:
#     x = 0
#     o = 0
#     for char in x_o:
#         if char == 'x' or char == 'X':
#             x = x + 1
#         elif char == 'o' or char == 'O':
#             o = o + 1
#     return x == o

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

# print(xo("zpzpzpp"))

# def validate_pin(pin: str) -> bool:
#     return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)
# print(validate_pin('-12345'))

# import datetime
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)
# print(current_datetime.weekday())
# print(current_datetime.isoweekday())
# print(current_datetime.isoformat())
# print(current_datetime.strftime('%d-%m-%Y %H:%M:%S'))
# print(current_datetime.strftime('%d-%m-%Y %I:%M:%S %p'))
# print(current_datetime.strftime('%d-%m-%Y %H:%M:%S %p'))

# print(current_datetime.date())
# print(current_datetime.time())

# import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)
# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# # Розбір дати і часу з об'єкта datetime
# date = combined_datetime.date()
# time = combined_datetime.time()

# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  

# from datetime import datetime, timezone, timedelta

# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC

# import time

# text = "Початок паузи"
# for char in text:
#     print(char, end='', flush=True)  # Виводимо символ без нового рядка
#     time.sleep(0.4 if char == ' ' else 0.1)  # 0.3 сек для пробілу, 0.1 сек для інших символів

# width = 5
# for num in range(18):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')

# if __name__ == '__main__': # Для воконання коду в поточному файлі

"""
Write a function, persistence, that takes in a positive parameter num and returns 
its multiplicative persistence, which is the number of times you must multiply the digits in num 
until you reach a single digit.
For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
"""
# def persistence(num: int) -> int:
#     count = 0  # Лічильник кроків
    
#     while num >= 10:  # Поки число не однозначне
#         product = 1
#         for digit in str(num):  
#             product *= int(digit)  # Перемножуємо цифри
#         num = product  # Оновлюємо num
#         count += 1  # Збільшуємо лічильник
    
#     return count
# from get_upcoming_birthdays import get_upcoming_birthdays, prepare_user_list
# users = [
#     {"name": "Андрій", "birthday": "1995.03.09"},
#     {"name": "Марія", "birthday": "2000.02.28"},
#     {"name": "Іван", "birthday": "1998.02.25"}
# ]
# print(get_upcoming_birthdays(prepare_user_list(users), 20))

# datetime.strptime(date_string, "%Y.%m.%d").date()
