class solution:
	@staticmethod
	def sumrow2D(matrix):
		for i in range(len(matrix)):
			sum=0
			for j in matrix[i]:
				sum=sum+j
			print(sum)
		
matrix=[[1,2,3],
	[4,5,6],
	[7,8,9]]
solution.sumrow2D(matrix)