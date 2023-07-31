def dec_to_hex(number):
    # Проверка на целое число
    if not isinstance(number, int):
        print("Введите целое число")
        return

    # Преобразование числа в шестнадцатеричное представление
    hex_string = hex(number)[2:]  # Используем срез, чтобы удалить приставку "0x"
    return hex_string


# Пример использования
input_number = int(input("Введите целое число: "))
result = dec_to_hex(input_number)

if result is None:
    pass  # Сообщение об ошибке уже отображено в функции dec_to_hex
else:
    print("Шестнадцатеричное представление числа:", result)
    print("Проверка с использованием функции hex:", hex(input_number)[2:])
