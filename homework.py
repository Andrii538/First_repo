# from datetime import datetime
    
# def get_days_from_today(date: str):
#     """
#     Розраховує кількість днів між заданою датою та сьогоднішнім днем.\n
#     Аргументи:
#     date (str): Дата у форматі 'YYYY-MM-DD' (наприклад, '2025-01-27').\n
#     Повертає:
#     int: Кількість днів від заданої дати до сьогоднішньої.\n
#     Якщо дата введена у неправильному форматі, повертає повідомлення про помилку.
#     """
#     today = datetime.now().date()  # Додаємо змінну today, призначаємо їй поточну дату і приводимо до типу date.
#     try:                    # Вводимо блок перевірки.
#         difference = datetime.strptime(date, "%Y-%m-%d").date() - today
#         # Вводимо нову змінну і присвоюємо їй резутьтат обрахунку різниці заданої дати і поточної.
#         return difference.days   # Виводимо результат, якщо формат заданої дати був відповвідний до 'РРРР-ММ-ДД'.
    
#     except ValueError:      # Опрацьовуємо помилку неправильного формату вхідних данних.
        
#         return "Дата має бути вказана у форматі: 'РРРР-ММ-ДД\'"  

# print(get_days_from_today('2025-10-09')) # Виводить 218


import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерує список унікальних випадкових чисел у заданому діапазоні.
    Аргументи:
    min (int): Мінімальне можливе число у наборі (не менше 1).\n
    max (int): Максимальне можливе число у наборі (не більше 1000).\n
    quantity (int): Кількість чисел у наборі.\n
    Повертає:
    list: Відсортований список унікальних випадкових чисел.
    Якщо параметри некоректні – повертає пустий список.
    """
    list_of_numbers = []    # Створюємо порожній список в який буде занесено фінальний результат.
    set_of_num = set()      # Створюємо множину, яка забезпечить унікальність чисел.
    if min < 1 or min >= max or max > 1000 or max - min + 1 < quantity:
        # Перевіряємо коректність заданих аргументів функції.
        return list_of_numbers      # Якщо якийсь з аргументів задано неправильно, повертаємо порожній список.
    else:
        while True:     # Використовуємо цикл while для повторення коду нижче до заданої умови True.
            if len(set_of_num) != quantity:
                set_of_num.add(random.randint(min, max))
                # Додаємо елементи до множини, поки їх кількість не дорівнюватиме заданому quantity.
            else:
                break   # Перериваємо цикл після досягнення умови.

    list_of_numbers = list(set_of_num)  # Перетворюємо множину в список і заносимо значення до фінального списку.
    list_of_numbers.sort()  # Сортуємо отриманий список.

    return list_of_numbers

lottery_numbers = get_numbers_ticket(100, 500, 401)
print("Ваші лотерейні числа:", lottery_numbers)


# import re

# def normalize_phone(phone_number: str) -> str:
#     cleaned_num = re.sub(r'[^0-9]', '', phone_number)  # Видаляємо всі нецифрові символи
#     prepared_num = re.sub(r'^38|^8', '', cleaned_num)  # Видаляємо '38' або '8' на початку
#     return '+38' + prepared_num  # Додаємо +38 перед номером




# import re

# def normalize_phone(phone_number: str) -> str:
#     """
#     Очищує телефонний номер і повертає стандартизований номер у форматі +380XXXXXXXXX.\n
#     Аргумент:
#     phone_number (str): рядок, що містить не стандартизований телефонний номер.\n
#     Повертає:
#     str: рядок, що містить очищений і стандартизований телефонний номер.
#     """
#     cleaned_num = re.sub(r'[^0-9+]', '', phone_number)  # Видаляємо всі нецифрові символи, крім знака +
    
#     if cleaned_num[:2] == '38':     # Перевіряємо, чи номер починається з 38
#         return '+' + cleaned_num    # Додаємо + і виводимо результат
#     elif cleaned_num[:3] == '+38':  # Перевіряємо, чи номер починається з +38
#         return cleaned_num          # Виводимо результат
#     elif cleaned_num[0] == '0':     # Перевіряємо, чи номер починається з 0
#         return '+38' + cleaned_num  # Додаємо +38 і виводимо результат
#     elif cleaned_num[0] == '8':    # Перевіряємо, чи номер починається з 8
#         return '+3' + cleaned_num   # Додаємо +38 і виводимо результат
#     else:
#         return "Некоректний номер"  # Якщо формат зовсім неправильний



# raw_numbers = [
#     "8067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# import time

# start = time.perf_counter()  # Початок вимірювання

# time.sleep(0.5)  # Імітація затримки (0.5 секунди)

# end = time.perf_counter()  # Кінець вимірювання
# elapsed_ms = (end - start) * 1000  # Конвертуємо в мс

# print(f"Час виконання: {elapsed_ms:.2f} мс")

