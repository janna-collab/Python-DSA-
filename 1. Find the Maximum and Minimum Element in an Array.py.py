class solution:
	@staticmethod
	def find_max (list1):
		max_val=list1[0]
		for i in list1:
			if max_val<i:
				max_val=i
		return max_val
		
	def find_min (list1):
		min_val=list1[0]
		for i in list1:
			if min_val>i:
				min_val=i
		return min_val

l=[4,9,5,1,2]
print("The maximum is :",solution.find_max(l))
print("The minimum is :",solution.find_min(l))