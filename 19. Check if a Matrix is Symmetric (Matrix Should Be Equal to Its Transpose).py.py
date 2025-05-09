class solution:
    def transpose(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for i in range(cols):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])
            result.append(new_row)
        return result
    def symetric_or_not(matrix):
        r=solution.transpose(matrix)
        if matrix==r:
            print("symetric")
        else:
            print("Asymetric")

matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
solution.symetric_or_not(matrix)


