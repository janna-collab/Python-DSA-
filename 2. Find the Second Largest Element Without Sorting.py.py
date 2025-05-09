class solution:
    @staticmethod
    def sl(arr):
        if len(arr)<2:
            return None
        f=float('-inf')
        s=float('-inf')
        for num in arr:
            if num>f:
                f=num
            elif num>s and num!=f:
                s=num
        return s if s!=float('-inf') else -1
arr=[12,35,1,10,34,1]
x=solution.sl(arr)
print(x)
    