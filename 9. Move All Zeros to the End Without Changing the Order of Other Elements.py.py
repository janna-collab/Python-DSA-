class solution:
	@staticmethod
	def movezero(arr):
		i=0
		for j in range(0,len(arr)):
			if arr[j]!=0:
				arr[i]=arr[j]
				i=i+1
		while i<len(arr):
			arr[i]=0
			i=i+1
			
		return arr
arr=[4,5,0,0,7,0,9,0,8]
print(solution.movezero(arr))