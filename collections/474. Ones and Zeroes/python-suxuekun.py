class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        # dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # c = [Counter(strs[k]) for k in range(l)]
        dp = [[0] * (n+1) for _ in range(m+1)]
        c=[[s.count("0"), s.count("1")] for s in strs]
        
        for k in range(l):
            ct = c[k]
            z = c[k][0]
            o = c[k][1]
            for i in range(m,z-1,-1):
                for j in range(n,o-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-z][j-o]+1)
            
        return dp[-1][-1]
        
        
#         l = len(strs)
#         dp = [[[0 for k in range(l)] for j in range(n+1)] for i in range(m+1)]
#         c = [[0 for t in range(2)] for k in range(l)]
#         for k in range(l):
#             for e in strs[k]:
#                 if e =="0":
#                     c[k][0]+=1
#                 else:
#                     c[k][1]+=1
        
#         for i in range(m+1):
#             for j in range(n+1):
#                 for k in range(l):
#                     if i>=c[k][0] and j>= c[k][1]:
#                         if k>0:
#                             dp[i][j][k] = max(dp[i][j][k-1],dp[i-c[k][0]][j-c[k][1]][k-1]+1)
#                         else:
#                             dp[i][j][k] = 1
#                     else:
#                         if k>0:
#                             dp[i][j][k] = dp[i][j][k-1]
#                         else:
#                             dp[i][j][k] = 0
        
#         # for i in range(m+1):
#         #     for j in range(n+1):
#         #         print(dp[i][j])
#         return dp[m][n][l-1];
        
        
        
        