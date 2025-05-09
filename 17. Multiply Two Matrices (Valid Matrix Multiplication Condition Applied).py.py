class solution:
    @staticmethod
    def multiply2d(m1,m2):
        m=len(m1)
        n=len(m2)
        p=len(m2[0])
        result=[[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j]+=m1[i][k]*m2[k][j]
        return result
    
m1= [
    [1, 2],
    [3, 4]
]

m2= [
    [5, 6],
    [7, 8]
]

for i in solution.multiply2d(m1,m2):
    print(i)
