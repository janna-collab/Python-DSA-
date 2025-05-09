class solution:
	@staticmethod
	def removeduplicate(arr):
		i=0
		for j in range(1,len(arr)):
			if arr[j]!=arr[i]:
				i=i+1
				arr[i]=arr[j]
		print("Unique elements are:",i+1)		
		return arr[:i+1]
		
arr=[4,4,5,5,6,7,8,8]
print(solution.removeduplicate(arr))