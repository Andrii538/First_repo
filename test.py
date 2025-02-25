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

text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = []
start = 0

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


