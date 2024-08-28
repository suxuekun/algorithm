class Solution:
    def intersec(self,n1,n2):
        s1 = set(n1);
        l = []
        for i in n2:
            if i in s1:
                l.append(i)
        return l
            
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            l = self.intersec(l,n)
        l.sort()
        return l
            
            
        
        
        