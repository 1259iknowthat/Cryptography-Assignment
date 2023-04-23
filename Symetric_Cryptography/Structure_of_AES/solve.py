def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    s = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s += chr(matrix[i][j])
    return s

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# print(matrix2bytes(matrix))
print(matrix2bytes(matrix))
