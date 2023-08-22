def print_matrix_integer(matrix):
    for row in matrix:
        row_str = ""
        for i, num in enumerate(row):
            if i > 0:
                row_str += " "
            row_str += "{:d}".format(num)
        print(row_str)