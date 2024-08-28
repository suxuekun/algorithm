class Solution:
    
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        l = len(nums)
        x = [0]*l
        count = 0
        for j in range(l):
            x[j] = nums[j]
            if x[j] ==k:
                count +=1;
            for i in range(j+1,l):
                x[i] = lcm(x[i-1],nums[i])
                print(x[i])
                if x[i] == k:
                    count +=1
                if x[i] >k:
                    break
        return count
       
        
        
        
        
        