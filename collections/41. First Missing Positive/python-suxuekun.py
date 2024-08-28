class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums);
        for i in range(l):
            while nums[i] != i+1 and  0 < nums[i] <= l and nums[i] != nums[nums[i]-1]:
                k = nums[i]
                nums[i],nums[k-1] = nums[k-1],nums[i]
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        return l+1
                