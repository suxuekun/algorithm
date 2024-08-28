class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        
        
        
        
        l = len(nums);
        h = []
        for i in range(l):
            h.append(0);
        for i in range(l):
            e = nums[i];
            step = i-e;
            if step < 0:
                step = l+step
            if step == l-1:
                continue
            h[step+1]+=1;
            
        sum = 0;
        for i in range(1,l):
            h[i] += h[i-1]
            
        
        m = 0;
        k = 0;
        for i in range(l):
            h[i] = i - h[i];
            if h[i] > m:
                m = h[i]
                k = i;
            
        return k
            
            
            
            
            
            
            
      
        
        

        
        
        