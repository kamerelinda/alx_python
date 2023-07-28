def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        # Create a new row for the squared_matrix and compute the square of each element
        squared_row = [num ** 2 for num in row]
        squared_matrix.append(squared_row)

    return squared_matrix
