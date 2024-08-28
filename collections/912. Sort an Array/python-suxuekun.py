class Solution:
    def quicksort(self,nums:List[int],i:int,j:int) ->List[int]:
        if i < j:
            k = self.partition(nums,i,j)
            self.quicksort(nums,i,k)
            self.quicksort(nums,k+1,j)
        return nums
    
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
            while i <= j and nums[i] < pivot:
                i += 1

            while i <= j and nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return i,j
    
    def partition(self,nums: List[int],i,j) ->int:
        t = i+(j-i)//2
        p = nums[t]
        nums[t],nums[i] = nums[i],nums[t]
        n = i
        for k in range(i+1,j):
            if nums[k] < p:
                n+=1;
                nums[k],nums[n] = nums[n],nums[k]
        nums[n], nums[i] = nums[i], nums[n]
        return n
    
    def quick_sort(self, nums):
        def quick_sort_helper(nums, left, right):
            if left >= right:
                return 
            
            i, j = left, right
            pivot = nums[random.randint(left, right)]
            
            while i <= j:
                while i <= j and nums[i] < pivot:
                    i += 1
                
                while i <= j and nums[j] > pivot:
                    j -= 1
                
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            quick_sort_helper(nums, left, j)
            quick_sort_helper(nums, i, right)
        
        quick_sort_helper(nums, 0, len(nums) - 1)
        
        return nums
    
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.quick_sort(nums)
        # return self.quicksort(nums,0,len(nums))
        return self.quicksort2(nums,0,len(nums)-1)
        
        
        
        