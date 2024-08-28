class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        f = (nums.pop()+nums.pop(0))/2
        while len(nums)>0:
            a = (nums.pop()+nums.pop(0))/2
            f = a if a < f else f
        return f
