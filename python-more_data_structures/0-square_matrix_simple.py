def square_matrix_simple(matrix):
    for row in matrix:
        new_matrix = []
        for i, num in enumerate(row):
            new_matrix.append([num ** 2])
        print(new_matrix)

# print(square_matrix_simple([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))