class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        g,h = {},{}
        for i in range(len(s)):
            x = g.get(s[i])
            y = h.get(t[i])
            if (x != y):
                return False
            if not x:
                g[s[i]] = i
                h[t[i]] = i
        return True