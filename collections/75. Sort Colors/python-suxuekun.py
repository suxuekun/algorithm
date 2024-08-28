class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums);
        i,k,j = 0,0,l-1;
        
        while k<=j:
            if nums[k] == 2:
                nums[k],nums[j] = nums[j],nums[k]
                j -=1;
                continue
            if nums[k] == 1:
                k+=1;
                continue
            if nums[k] == 0:
                nums[k],nums[i] = nums[i],nums[k]
                i+=1;
                if k < i:
                    k=i;
        return nums;
            
        
        
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        