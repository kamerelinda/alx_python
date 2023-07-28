def square_matrix_simple(matrix=[[]]):
    def sq(num):
        return num * num
    for row in matrix:
        far = list(map(sq, row))
        print(far, end=', ')

