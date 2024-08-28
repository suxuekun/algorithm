class Solution:
    def rob(self, nums: List[int]) -> int:
        pre,now = 0,0;
        for i in nums:
            now,pre = max(now, pre + i),now
        return now 