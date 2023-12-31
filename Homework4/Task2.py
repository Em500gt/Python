# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление. Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def rev_kwargs(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        if hash(key) is None:
            key_string = str(key)
        else:
            key_string = key
        value = str(value)
        result[value] = key_string
    return result

print(rev_kwargs(res=1, reverse=[1, 2, 3]))