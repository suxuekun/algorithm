class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n+1)]for j in range(m+1)]

        k = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                    if (dp[i][j] > k):
                        k = dp[i][j]
        
        return k*k


    # def maximalSquare(self, matrix: List[List[str]]) -> int:
        # m = len(matrix)
        # n = len(matrix[0])

        # dp = [[0 for i in range(n+1)] for j in range(m+1)]

        # dp[0][0] = int(matrix[0][0])

        # largest = dp[0][0]
        # for i in range(1,m):
        #     dp[i][0] = int(matrix[i][0])
        #     if dp[i][0] > largest:
        #         largest = dp[i][0]
        # for i in range(1,n):
        #     dp[0][i] = int(matrix[0][i])
        #     if dp[0][i] > largest:
        #         largest = dp[0][i]

        
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if matrix[i][j] == "1":
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
        #             if dp[i][j] > largest:
        #                 largest = dp[i][j]
        #         else:
        #             dp[i][j] = 0
        # for k in dp:
        #     print(k)
        # return largest*largest
