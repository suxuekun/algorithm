class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1 :
            return 0
        for i in range(1,l):
            nums[i] = nums[i] + nums[i-1]
        s = nums[-1]
        print (s,nums)
        if s- nums[0] == 0:
            return 0
        for i in range(1,l):
            if nums[i-1] == s - nums[i]:
                return i
        return -1
            