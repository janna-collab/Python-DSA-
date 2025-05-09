class solution:
	@staticmethod
	def print2D(matrix):
		for i in range(len(matrix)):
			for j in matrix[i]:
				print(j ,end=" ")
			print()
matrix=[[1,2,3],
	[4,5,6],
	[7,8,9]]
solution.print2D(matrix)
