def is_prime(number):
    # Проверка на отрицательное число и число больше 100000
    if number < 0 or number > 100000:
        print("Число должно быть положительным и не превышать 100000")
        return

    # Проверка на простоту числа
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Пример использования
input_number = int(input("Введите число: "))
result = is_prime(input_number)

if result is None:
    pass  # Сообщение об ошибке уже отображено в функции is_prime
elif result:
    print("Число является простым")
else:
    print("Число является составным")