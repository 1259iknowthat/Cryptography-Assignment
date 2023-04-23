state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):


    """"
    s=sum(s, [])
    k=sum(k, [])
    mat=[s[i] ^ k[i] for i in range(len(s))]
    return [list(mat[i:i+4]) for i in range(0, len(mat), 4)]
    """
    
    return [[a^b for a, b in zip(i, j)] for i, j in zip(s, k)]
    
    
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

matrix=add_round_key(state, round_key)
print(matrix2bytes(matrix))


