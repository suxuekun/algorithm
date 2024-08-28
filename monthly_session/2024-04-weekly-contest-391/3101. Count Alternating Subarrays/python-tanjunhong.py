class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        left = 0
        current = 1
        for right in range(1,len(nums)):
            if nums[right] == nums[right - 1]:
                left = right
                current += 1
            else:
                current += right - left + 1
        return current