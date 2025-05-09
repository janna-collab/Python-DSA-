class solution:
	@staticmethod
	def count_even_odd(arr):
		count_even=0
		count_odd=0
		for num in arr:
			if num%2==0:
				count_even=count_even+1
			else:
				count_odd=count_odd+1
		print("The even no count is:",count_even)
		print("The odd no count is:",count_odd)

arr=[2,4,3,5,6,1,0,4]
solution.count_even_odd(arr)


		