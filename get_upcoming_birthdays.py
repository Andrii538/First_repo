# from datetime import datetime, date, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list


# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)


# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#     return birthday


# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year=today.year + 1)
#         if 0 <= (birthday_this_year - today).days <= days:
#             birthday_this_year = adjust_for_weekend(birthday_this_year)
#             congratulation_date_str = date_to_string(birthday_this_year)
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#     return upcoming_birthdays

from datetime import datetime, timedelta, date

def find_next_weekday(start_date: date, weekday: int) -> date:
    """Знаходить наступний вказаний день тижня."""
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def string_to_date(date_string: str) -> date:
    """Перетворює дату у форматі 'YYYY.MM.DD' у об'єкт datetime.date."""
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date_obj: date) -> str:
    """Перетворює дату у форматі datetime.date в рядок 'YYYY.MM.DD'."""
    return date_obj.strftime("%Y.%m.%d")

def prepare_user_list(user_data: list) -> list:
    """Перетворює список користувачів із датами-рядками у список з datetime.date."""
    prepared_list = []
    for user in user_data:
        try:
            birthday = string_to_date(user["birthday"])
            prepared_list.append({"name": user["name"], "birthday": birthday})
        except ValueError:
            print(f"⚠️ Пропущено некоректну дату: {user['birthday']} у {user['name']}")
    return prepared_list


def adjust_for_weekend(birthday: date) -> date:
    """Якщо день народження випадає на вихідний, переносимо на понеділок."""
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)  # Понеділок
    return birthday

def get_upcoming_birthdays(users: list, days: int = 7) -> list:
    """Знаходить найближчі дні народження та повертає список привітань."""
    upcoming_birthdays = []
    today = date.today()
    
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)  # Перевіряємо поточний рік

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Якщо ДН вже минув

        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Андрій", "birthday": "1995.03.01"},
        {"name": "Марія", "birthday": "2000.02.28"},
        {"name": "Іван", "birthday": "1998.02.26"}
    ]
    print(get_upcoming_birthdays(prepare_user_list(users), 20))
