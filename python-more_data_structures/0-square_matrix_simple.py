def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num ** 2)
        squared_matrix.append(squared_row)
    return squared_matrix

# print(square_matrix_simple([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))