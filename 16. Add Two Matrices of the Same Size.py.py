class solution:
	@staticmethod
	def two2dsum(m1,m2):
		c=[]
		for i in range(len(m1)):
			row=[]
			for j in range(len(m1[0])):
				row.append(m1[i][j]+m2[i][j])
			c.append(row)
		return c
	
	
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]

output = solution.two2dsum(matrix1, matrix2)
for row in output:
    print(row)
