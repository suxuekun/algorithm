class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        p = k+l
        i = 0
        
        list1={}
        list2={}
        
        while i<l:
            item = nums[i]
            if k < item < p:
                list2[item] = True
            if item <=k:
                list1[item] = True
            i+=1
        
        
        l = len(list1.keys())
        
        # print(list1.keys(),list2.keys())
        
        
        while True:
            dels = []
            for i in list2:
                if i <= k+l:
                    list1[i] = True
                    dels.append(i)
            if not len(dels):
                break
            for i in dels:
                del list2[i]
            
            l = len(list1.keys())
           
       
        k = k+l
        s1 = k*(k+1)//2
        # print(k)
        s2 = 0
        for j in list1:
            s2 +=j
        
        s = s1-s2
        return s
        
                
            
                
            
                
        
                
            
        