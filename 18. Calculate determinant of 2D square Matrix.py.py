class Solution:
    @staticmethod
    def minor(matrix, row, col):
        return [r[:col] + r[col+1:] for i, r in enumerate(matrix) if i != row]

    @staticmethod
    def determinant(matrix):
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        det = 0
        for col in range(n):
            sign = (-1) ** col
            minor = Solution.minor(matrix, 0, col)
            det += sign * matrix[0][col] * Solution.determinant(minor)

        return det



matrix = [
    [4, 2, 1],
    [3, 5, 2],
    [2, 1, 3]
]

print("Determinant:", Solution.determinant(matrix))
