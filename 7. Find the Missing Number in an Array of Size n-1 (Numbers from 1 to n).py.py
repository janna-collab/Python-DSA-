class solution:
	def missnum(arr,n):
		sum=0
		sumf=n*(n+1)/2
		for i in arr:
			sum=sum+i
		return sumf-sum
arr=[2,3,4,5,6]
n=6
print(solution.missnum(arr,n))
			