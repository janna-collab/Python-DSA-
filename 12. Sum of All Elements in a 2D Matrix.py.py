class solution:
	@staticmethod
	def sum2D(matrix):
		sum=0
		for i in range(len(matrix)):
			for j in matrix[i]:
				sum=sum+j
		return sum
matrix=[[1,2,3],
	[4,5,6],
	[7,8,9]]
print(solution.sum2D(matrix))