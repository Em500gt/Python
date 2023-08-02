# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.


def calculation(backpack, carrying):

    result = set()
    count = carrying

    for k, v in backpack.items():
        if k not in result and count >= v:
            result.add(k)
            count -= v    

    return result


backpack = {"спальник": 5, "палатка": 10, "еда": 3, "вода": 4, "фонарик": 2, "карта": 1, "нож": 1, "топор": 5}
carrying = 20

print(calculation(backpack, carrying))