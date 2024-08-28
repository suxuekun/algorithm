class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1
        if n < 2:
            return 0
        k = int(n**0.5)
        dp1 = [n//i for i in range(1,k+1)]
        dp2 = list(range(dp1[-1]-1,0,-1))
        dp = {x:x-1 for x in dp1+dp2}

        for i in range(2,k+1):
            if dp[i] == dp[i-1]:
                continue
            i2 = i*i
            p = dp[i-1]
            for j in dp:
                if j < i2:
                    break
                dp[j] = dp[j] - dp[j//i] + p
        
        return dp[n]
                
