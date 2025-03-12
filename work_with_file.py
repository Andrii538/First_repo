# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")

# from pathlib import Path

# Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# Бінарні дані для запису
# data = b"Python is great!"

# Запис байтів у файл
# file_path.write_bytes(data)

# Читання байтів з файлу
# binary_data = file_path.read_bytes()
# print(binary_data)

# path = Path("example.bin")

# # Перевірка існування
# if path.exists():
#     print(f"{path} існує")

# # Перевірка, чи це директорія
# if path.is_dir():
#     print(f"{path} є директорією")

# # Перевірка, чи це файл
# if path.is_file():
#     print(f"{path} є файлом")
# size = file_path.stat().st_size
# print(f"Розмір файла: {size} байтів")

# file_path = Path('/path/to/file.txt')
# file_path.unlink(missing_ok=True)
# with open('test.txt', 'r') as fh:
#     print(fh.read())
# import sys
# print(sys.modules["os"].__file__)

# from goit_algo_hw_04_01 import total_salary
# # print(total_salary('goit_algo_hw_04_01_data.txt'))
# total, average = total_salary("path/to/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# contacts = {'Jone': '0635346696', 'Bob': '0564556896'}

def show_phone(name):
    contacts = {'Jone': '0635346696', 'Bob': '0564556896'}
    if name in contacts:
        return contacts[name]
    else:
        return "Name not found."
    
print(show_phone('Bob'))