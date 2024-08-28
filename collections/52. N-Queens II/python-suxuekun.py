class Solution:
    def totalNQueens(self, n: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(n)]

        global count
        count = 0

        def copy(m):
            return [[x for x in m[i]] for i in range(n)]
        
        def backtrack(matrix,i):
            global count
            if (i == n):
                count +=1
                # res.append(matrix)
                return
            for j in range(n):
                if matrix[i][j] == 0:
                    m = copy(matrix)
                    for k in range(n):
                        m[k][j] = 1
                        m[i][k] = 1
                    for k in range(1,n-i):
                        if j-k>=0:
                            m[i+k][j-k] = 1
                        if j+k<n:
                            m[i+k][j+k] = 1
                    backtrack(m,i+1)
        
        backtrack(matrix,0)
        return count
        

        
        