class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                return 1
            return 0

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)

        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)        

        count =0
        for i in range(1,m-1):
            for j in range(n):
                count += dfs(i,j)
        return count