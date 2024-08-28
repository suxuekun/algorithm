class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # sort 
        nums.sort()
        
        # get n 
        n = len(nums)//2
        
        # special case for 2 length
        if n == 1:
            return [(nums[0] + nums[1]) //2]
        
        
        p = 1;
        q = 2 * n -2
        
        # find a possible K ( K here actually should be 2k )
        while p <=n :
            # find a K from lower side 
            k = nums[p] - nums[0]
            # k should be 2 4 6 8 .... so even number exclude 0 
            if k < 2 or k % 2 == 1:
                p +=1;
                continue
                
            # should find same K on higher side or it is not a possible k 
            while nums[-1] - nums[q] < k:
                q-=1;
            if nums[-1] -nums[q] == k:
                # find a solotion of k 
                # res = self.find(nums,k,p,n)
                res = self.find2(nums,k)
                
                if res:
                    return [i +k//2 for i in res]
            p+=1;
        return []
    
    def find2(self,nums,k):
        
        num_counter = Counter(nums)
        output = []
        for low in nums:
            if num_counter[low] <= 0:
                continue
            comp_low = low + k
            num_counter[low] -= 1
            num_counter[comp_low] -= 1
            output.append(low)

        if len(output) == len(nums) / 2:            
            return output
        else:
            return False
    
    # find a solution of k 
    def find(self,nums,k,q,n):
        # prepare the lower 
        lower = []
        # p is pointer of lower array
        p = 0
        # i ,j is pointer of nums array from nums [i,i+1,i+2...j-1] should be long to lower and nums[j] should be long to higher array and 
        # nums[j] here is right be higher[p] 
        
        i = 0
        j = q  # nums[q] is higher[0] the first higher item
        
        while len(lower) < n:
            # first lower items 
            for _ in range(i,j):
                lower.append(nums[_])
            j = i = j+1
            p+=1;
            
            # lower more than n items failed case.
            if len(lower) > n:
                return False
            
            
            # if not enough item in lower , add the next item to lower array
            if len (lower) <n:
                if len(lower) <= p:
                    lower.append(nums[j])
                    i+=1;
                    j+=1;
            
            # find next nums[j] as higher[p] which nums[j] - lower[p] = K
            if p <= len(lower) :        
                while j < len(nums)-1 and nums[j] - lower[p] < k:
                    j+=1;
                if nums[j] - lower[p] > k:
                    return False;
        # when lower find n element 
        # then the rest should be in higher array
        # all remaining numbers in nums need to check nums[j] - lower[p] = k
        if len(lower) > n:
            return False
        else:
            while (p<n):
                if j >= 2*n:
                    return False
                if nums[j] - lower[p] !=k:
                    return False;
                p +=1;
                j +=1;
        return lower