class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def kmp(s1,s2):
            next = cal_next(s2)
            #print(s2)
            #print(next)
            j = -1
            for i in range(len(s1)):
                while j>-1 and s1[i] != s2[j+1]:
                    j = next[j]
                if s1[i] == s2[j+1]:
                    j = j+1
                if j == len(s2) -1:
                    return i-j
            return -1
        def cal_next(s):
            next = [-1]
            j = -1
            num = 0
            for i in range(1,len(s)):
                while j>-1 and s[i] != s[j+1]:
                    j = next[j]
                if s[i] == s[j+1]:
                    j = j+1
                next.append(j)
            return next
        return kmp(haystack,needle)
