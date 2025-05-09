class Solution:
    @staticmethod
    def transposesquare(matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    @staticmethod
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


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("In-place transpose of square matrix:")
for row in Solution.transposesquare(matrix1):
    print(row)

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]

print("\nNew matrix transpose (non-square):")
for row in Solution.transpose(matrix2):
    print(row)
