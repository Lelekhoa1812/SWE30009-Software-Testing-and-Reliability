# mutation2.py
def matrix_multiply_recursive(matrix_a, matrix_b):
    if not matrix_a or not matrix_b:
        return []
    if not all(
        (len(matrix_a) == len(matrix_b), is_square(matrix_a), is_square(matrix_b))
    ):
        raise ValueError("Invalid matrix dimensions")

    result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    def multiply(i_loop, j_loop, k_loop, matrix_a, matrix_b, result):
        if i_loop >= len(matrix_a):
            return
        if j_loop >= len(matrix_b[0]):
            return multiply(i_loop + 1, 0, 0, matrix_a, matrix_b, result)
        if k_loop >= len(matrix_b):
            return multiply(i_loop, j_loop + 1, 0, matrix_a, matrix_b, result)
        result[i_loop][j_loop] += matrix_a[k_loop][i_loop] * matrix_b[k_loop][j_loop] # Bug: swapped index in matrix_a (Change of array index)
        return multiply(i_loop, j_loop, k_loop + 1, matrix_a, matrix_b, result)

    multiply(0, 0, 0, matrix_a, matrix_b, result)
    return result

def is_square(matrix):
    len_matrix = len(matrix)
    return all(len(row) == len_matrix for row in matrix)