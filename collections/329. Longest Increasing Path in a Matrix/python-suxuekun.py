class Solution:
    
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i,j,matrix):
            if dp[i][j]:
                return dp[i][j];
            ml = 1 
            if i>0 and matrix[i][j] < matrix[i-1][j]:
                ml = max(ml,dfs(i-1,j,matrix)+1)
            if i<m-1 and matrix[i][j] < matrix[i+1][j]:
                ml = max(ml,dfs(i+1,j,matrix)+1)
            if j>0 and matrix[i][j] < matrix[i][j-1]:
                ml = max(ml,dfs(i,j-1,matrix)+1)
            if j<n-1 and matrix[i][j] < matrix[i][j+1]:
                ml = max(ml,dfs(i,j+1,matrix)+1)
            dp[i][j] = ml
            return ml
    
        m = len(matrix)
        n = len(matrix[0]);
        dp = [[ 0 for j in range(n)] for i in range(m)]
        
        ml = 0;
        for i in range(m):
            for j in range(n):
                if dp[i][j] > 0:
                    continue
                ml = max(ml,dfs(i,j,matrix))
        return ml;