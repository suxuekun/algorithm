class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        j = 0
        l = 0
        n = 0
        for i in range(len(s)):
            c = s[i]
            if d.get(c) and d[c]>=j:
                j = d[c]
                
            else:
                n = i-j +1
                if n >l:
                    l = n
            d[c] = i+1

        return l