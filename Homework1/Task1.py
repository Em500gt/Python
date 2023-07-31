def check_triangle(a, b, c):
    # Проверка существования треугольника
    if a + b > c and a + c > b and b + c > a:
        # Проверка типа треугольника
        if a == b and b == c:
            return "Треугольник является равносторонним"
        elif a == b or a == c or b == c:
            return "Треугольник является равнобедренным"
        else:
            return "Треугольник является разносторонним"
    else:
        return "Треугольник не существует"
    
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

result = check_triangle(a, b, c)
print(result)