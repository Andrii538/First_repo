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

