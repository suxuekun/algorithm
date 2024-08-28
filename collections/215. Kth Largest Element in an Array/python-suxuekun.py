class Solution:
    
    def heapsolution(self,nums,k):
        c = 0
        h = []
        for i in nums:
            if c<k:
                heappush(h,i)
            else:
                heappushpop(h,i)
            c+=1;
        return heappop(h)
    
    def quicksort(self,nums:List[int],i:int,j:int) ->List[int]:
        if i < j:
            k = self.partition(nums,i,j)
            self.quicksort(nums,i,k)
            self.quicksort(nums,k+1,j)
        return nums
    
    def partition(self,nums: List[int],i,j) ->int:
        t = random.randint(i, j-1)
        
        p = nums[t]
        nums[t],nums[i] = nums[i],nums[t]
        n = i
        for k in range(i+1,j):
            if nums[k] > p:
                n+=1;
                nums[k],nums[n] = nums[n],nums[k]
        nums[n], nums[i] = nums[i], nums[n]
        return n
    def quickfind(self,nums,i,j,k):
        pass
        
    def quicksort2(self,nums:List[int],i:int,j:int) ->List[int]:
        if i < j:
            p,q = self.partition2(nums,i,j)
            self.quicksort2(nums,i,q)
            self.quicksort2(nums,p,j)
        return nums
    
    def partition2(self,nums,left,right):
        i, j = left, right
        pivot = nums[random.randint(left, right)]

        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1

            while i <= j and nums[j] < pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return j
    def quickfind2(self,nums,i,j,k):
        if i < j:
            p = self.partition(nums,i,j)
            if p > k-1:
                return self.quickfind2(nums,i,p,k)
            if p < k-1:
                return self.quickfind2(nums,p+1,j,k)
        
            return nums[p]
           
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heapsolution(nums,k)
        # return self.quickfind2(nums,0,len(nums),k)
        