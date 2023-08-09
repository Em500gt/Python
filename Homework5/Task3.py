# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b


print(*fib_gen(10))
