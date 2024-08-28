class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        def dfs(i,j):
            grid2[i][j] = 0
            res = grid1[i][j]
            if j-1 >=0 and grid2[i][j-1] == 1:
                res &= dfs(i,j-1)
            if j+1 <n and grid2[i][j+1] == 1:
                res &= dfs(i,j+1)
            if i-1 >=0 and grid2[i-1][j] == 1:
                res &= dfs(i-1,j)
            if i+1 <m and grid2[i+1][j] == 1:
                res &= dfs(i+1,j)
            
            return res

        c = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    l = [[i,j]]
                    print(i,j)
                    grid2[i][j] = 0
                    c += dfs(i,j)
        return c
        




    #     m = len(grid1)
    #     n = len(grid1[0])
    #     for i in range(m):
    #         for j in range(n):
    #             grid2[i][j] += grid1[i][j] + grid2[i][j]
        
    #     # for r in grid2:
    #     #     print(r)

    #     c = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid2[i][j] == 3:
    #                 l = [[i,j]]
    #                 grid2[i][j] = -1
    #                 c += self.bfs(grid2,l)
    #     return c

    # def bfs(self,grid : List[List[int]],l) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     res = 1
    #     while len(l) >0:
    #         i = l[0][0]
    #         j = l[0][1]
            

    #         left = i-1
    #         right = i+1
    #         top = j-1
    #         bot = j+1
    #         pos = [[i,top],[i,bot],[left,j],[right,j]]
    #         for p in pos:
    #             x = p[0]
    #             y = p[1]
    #             if (0<=x < m )and (0<=y < n):
    #                 if grid[x][y] == 3:
    #                     grid[x][y] = -1
    #                     l.append([x,y])
    #                 if grid[x][y] == 2:
    #                     res = 0
    #         l.pop(0)
    #     return res
                            

        