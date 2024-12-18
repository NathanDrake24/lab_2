def get_number():

    for i in range(30):
        if i % 2 != 0:
            yield i



if __name__ == "__main__":
    numbers = get_number()

    first = next(numbers)
    print(f"Первое нечетное число: {first}")

    for _ in range(3): # Пропускаем 4 числа после первого
      next(numbers)

    fifth = next(numbers)
    print(f"Пятое нечетное число: {fifth}")

    # Находим последнее число, используя list для полного извлечения значений генератора
    all_numbers = list(numbers)
    last = all_numbers[-1] if all_numbers else None  # Обработка пустого списка

    if last is not None:
        print(f"Последнее нечетное число: {last}")
    else:
        print("Список нечетных чисел пуст.")

