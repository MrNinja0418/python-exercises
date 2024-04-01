def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0
    size = len(matrix)
    
    # Sum up elements on the TL-to-BR diagonal
    for i in range(size):
        total += matrix[i][i]
    
    # Sum up elements on the BL-to-TR diagonal
    for i in range(size):
        total += matrix[i][size - 1 - i]
    
    return total