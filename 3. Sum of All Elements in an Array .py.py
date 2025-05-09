class solution:
	@staticmethod
	def sumarr(arr):
		sum=0
		for i in arr:
			sum=sum+i
		return sum
arr=[3,4,2,1,6]
print("The sum of array is:",solution.sumarr(arr))	