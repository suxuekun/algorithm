class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # """
        # Do not return anything, modify matrix in-place instead.
        # """
        # n = len(matrix)
        # l = n//2

        # for i in range(l):
        #     for j in range(i,n-1-i):
        #         matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] = matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]

        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i):
        #         matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # for i in range(n):
        #     matrix[i].reverse()

        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]



