class solution:
	@staticmethod
	def sumcolumn2D(matrix):
		for i in range(len(matrix[0])):
			sum=0
			for j in range(len(matrix)):
				sum=sum+matrix[j][i]
			print(sum)		
matrix=[[1,2,3],
	[4,5,6],
	[7,8,9]]
solution.sumcolumn2D(matrix)