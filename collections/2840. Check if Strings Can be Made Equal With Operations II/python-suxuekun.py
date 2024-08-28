class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # def h(s:str) -> dict:
        #     res = {}
        #     for i in s:
        #         if not res.get(i):
        #             res[i] = 1
        #         else:
        #             res[i] +=1
        #     return res
        
        h = Counter

        a = h(s1[::2])
        b = h(s2[::2])
        c = h(s1[1::2])
        d = h(s2[1::2])
        return a == b and c == d
        