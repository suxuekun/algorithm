class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        (arr1,arr2) = (nums1,nums2) if len(nums1)<len(nums2) else (nums2,nums1)
        
        l1 = len(arr1)
        l2 = len(arr2)
        l = l1+l2
        one = l%2 == 1
        print (one)
        
        left = 0
        right = l1
        
        infinity = 2**30
        
        median1,median2 = 0,0
        
        while left <= right:
            i = (left+right)//2
            j = (l+1)//2 - i
            
            m = arr1[i-1] if i>0 else -infinity
            n = arr2[j-1] if j>0 else -infinity
            
            p = arr1[i] if i<l1 else infinity
            q = arr2[j] if j<l2 else infinity
            
            if m < q:
                median1 = max(m,n)
                median2 = min(p,q)
                left = i + 1
            else:
                right = i - 1
           
                
        return median1 if one else (median1+median2)/2