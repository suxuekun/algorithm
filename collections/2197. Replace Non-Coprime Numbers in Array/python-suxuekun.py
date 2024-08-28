class Solution:
    
    def gcd(n1,n2):
        return gcd(n2, n1 % n2) if n2 > 0 else n1
    
    # def lcm(n1,n2):
    #     return n1 * n2 // gcd(n1, n2)
    
    def lcm(n1,n2,gcd):
        return n1 * n2 // gcd;
    
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        l = len(nums);
        i = 0;
        while (i<l-1):
            a,b = nums[i],nums[i+1]
            g = gcd(a,b);
            
            if g > 1:
                rep = lcm(a,b,g)
                nums.pop(i)
                nums[i] = rep
                l -= 1
                if i > 0:
                    i -=1
            else:
                i +=1;
        return nums
            
        
        