class solution:
	@staticmethod
	def reversearr(arr):
		left=0
		right=len(arr)-1
		while left<right:
			arr[left],arr[right]=arr[right],arr[left]
			left=left+1
			right=right-1
		return arr
arr=[3,4,5,6]
print("The reverse array is",solution.reversearr(arr))
