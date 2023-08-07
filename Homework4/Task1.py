# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transposematrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

lst = [[1, 2, 3], [4, 5, 6]]

print(transposematrix(lst))