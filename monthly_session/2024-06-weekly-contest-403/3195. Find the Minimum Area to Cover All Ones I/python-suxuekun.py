class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        a = c = 1001
        b = d = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    a = min(a,i)
                    b = max(b,i)
                    c = min(c,j)
                    d = max(d,j)
        print(a,b,c,d)
        return (b-a+1)*(d-c+1)