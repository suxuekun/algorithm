class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        p = 0 
        s = 0
        a = 0
        for i in range(l):
            if height[i] >= p:
                p = height[i]
                s += a
                a = 0
            else:
                amount = p-height[i]
                a += amount
        p = 0
        a = 0

        for i in range(l-1,-1,-1):
            if height[i] > p:
                p = height[i]
                s += a
                a = 0
            else:
                amount = p-height[i]
                a += amount
        return s

            

        