def bytes2matrix(data):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    for i in range(4):
        for j in range(4):
            text[i][j] = ord(data[i].decode())
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

text = [[]]
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    for i in matrix:
        for j in i:
            print(j.to_bytes(1, 'big').decode(), end= "")    
            # text.append(j.to_bytes(1, 'big'))
    # return [list(text[i:i+4]) for i in range(0, len(text), 4)]

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# print(matrix2bytes(matrix))
for i in matrix2bytes(matrix):
    print(i.decode(),end="")
