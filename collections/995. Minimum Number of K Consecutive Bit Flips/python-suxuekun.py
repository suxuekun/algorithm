class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        i = 0;
        n = len(nums);
        dp = [0 for _ in range(n)]
        c = 0;
        f = 0;
        for i in range(n-k+1):
            if f == nums[i]:
                dp[i+k-1] = 1
                c +=1
            if dp[i+k-1] != dp[i]:
                f = not f
        j = n-1
        f = 0;
        while j>n-k:
            f = f != dp[j];
            if nums[j] == f:
                return -1
            j-=1;
        return c;