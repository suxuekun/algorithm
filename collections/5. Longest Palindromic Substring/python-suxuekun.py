class Solution:
    def prepare(self,s):
        return "#"+"#".join(s)+"#"
    def findpalindrome(self,s,c,n):
        l = len(s)
        left = c-n
        right = c+n
        while True:
            left -=1
            right +=1
            if left < 0:
                break
            if right >= l:
                break;
            if s[left] != s[right]:
                break
        return right-1

    def longestPalindrome(self, s: str) -> str:
        prepared_s = self.prepare(s)
        l = len(prepared_s)
        p = [0] * l
        c,r = 0,0
        i = 1
        while i < l:
            r2 = 0
            if i <= r:
                mirror_i = c-(i-c)
                if i + p[mirror_i] < r:
                    p[i] = p[mirror_i]
                else:
                    r2 = self.findpalindrome(prepared_s,i,r-i)
            else:
                r2 = self.findpalindrome(prepared_s, i, 0)
            if r2:
                p[i] = r2 - i
                if r2 > r:
                    c = i
                    r = r2
            i = i+1
        m = max(p)
        c = p.index(m)
        left = (c - m)//2
        right = (c + m)//2
        res = s[left:right]
        return res