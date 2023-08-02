# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def get_duplicates(nums):
    unique_nums = set()
    duplicates = []
    
    for num in nums:
        if num in unique_nums:
            duplicates.append(num)
        else:
            unique_nums.add(num)
    
    return duplicates

nums = [1, 2, 3, 1, 2, 4, 5]
result = get_duplicates(nums)
print(result)