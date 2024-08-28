class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [i//k for i in nums1 if i%k==0 ]
        s = 0

        n1 = Counter(nums)
        n2 = Counter(nums2)

        s1 = set(n1)
        s2 = set(n2)

        for i in s1:
            p = int(math.sqrt(i))
            
            for j in range(1,p+1):
                if i % j == 0:
                    if j in s2:
                        s += n1[i]*n2[j]
                    q = i//j
                    if q!=j and q in s2:
                        s += n1[i]*n2[q]
        return s

