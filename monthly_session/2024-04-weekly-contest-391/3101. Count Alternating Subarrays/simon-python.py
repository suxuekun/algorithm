class Solution:
    def countAlternatingSubarrays(self, nums):
        pointer = 0
        longest_segment = []
        segment_length = 1

        while pointer < len(nums) - 1:
            left = nums[pointer]
            right = nums[pointer + 1]
            if left != right:
                segment_length += 1
            else:
                longest_segment.append(segment_length)
                segment_length = 1

            pointer += 1
        longest_segment.append(segment_length)

        print(longest_segment)

        return sum([sum(range(i+1)) for i in longest_segment])