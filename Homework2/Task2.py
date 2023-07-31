from fractions import Fraction

def calculate_fractions_sum_product(fraction1, fraction2):
    try:
        numerator1, denominator1 = map(int, fraction1.split('/'))
        numerator2, denominator2 = map(int, fraction2.split('/'))
        
        # Создание объектов Fraction из числителя и знаменателя
        frac1 = Fraction(numerator1, denominator1)
        frac2 = Fraction(numerator2, denominator2)
        
        # Вычисление суммы и произведения дробей
        sum_fraction = frac1 + frac2
        product_fraction = frac1 * frac2
        
        return sum_fraction, product_fraction
    except ValueError:
        print("Введите две дроби в формате 'a/b'")
        return

# Пример использования
input_fraction1 = input("Введите первую дробь в формате 'a/b': ")
input_fraction2 = input("Введите вторую дробь в формате 'a/b': ")
result = calculate_fractions_sum_product(input_fraction1, input_fraction2)

if result is None:
    pass  # Сообщение об ошибке уже отображено в функции calculate_fractions_sum_product
else:
    sum_fraction, product_fraction = result
    print("Сумма дробей:", sum_fraction)
    print("Произведение дробей:", product_fraction)
    print("Проверка с использованием модуля fractions:")
    print("Сумма:", Fraction(input_fraction1) + Fraction(input_fraction2))
    print("Произведение:", Fraction(input_fraction1) * Fraction(input_fraction2))
