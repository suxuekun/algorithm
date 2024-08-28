class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a = s1[::2]
        b = s2[::2]
        c = s1[1::2]
        d = s2[1::2]

        return (a == b or a==b[::-1] ) and (c==d or c==d[::-1])
        