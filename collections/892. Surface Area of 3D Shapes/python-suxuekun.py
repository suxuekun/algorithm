class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = 0;
        s = 0;
        t = 0;
        l = len(grid)
        for i in range(l):
            lj = len(grid[i])
            for j in range(lj):
                v = grid[i][j]
                if v:
                    t +=1;
                    r += v
                    s +=min(v,grid[i-1][j]) if i else 0
                    s +=min(v,grid[i][j-1]) if j else 0 
        return 4*r - 2*s + 2*t