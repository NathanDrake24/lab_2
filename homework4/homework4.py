import random


def find_multiples(x):
    if x == 0:
        return None
    numbers = [random.randint(0, 200) for _ in range(random.randint(10, 20))]
    print(f"Сгенерированный список чисел: {numbers}")

    multiples = list(filter(lambda num: num % x == 0, numbers))
    return multiples


if __name__ == "__main__":
    try:
        x = int(input("Введите число X: "))
        multiples = find_multiples(x)
        if multiples is not None:
            print(f"Числа, кратные {x}: {multiples}")
        else:
            print("Деление на ноль недопустимо.")

    except ValueError:
        print("Некорректный ввод. Введите целое число.")

