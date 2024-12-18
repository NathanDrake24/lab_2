import datetime

def calculate_age(birthdate):
    try:
        day, month, year = map(int, birthdate.split('/'))
        birthdate_obj = datetime.date(year, month, day)
        today = datetime.date.today()
        age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))
        return age
    except ValueError:
        return None

if __name__ == "__main__":
    birthdate_str = input("Введите вашу дату рождения в формате ДД/ММ/ГГГГ: ")
    age = calculate_age(birthdate_str)

    if age is not None:
        print(f"Ваш возраст: {age} лет")
    else:
        print("Неверный формат даты.")


