class Solution:
    def compressedString(self, word: str) -> str:
        s = word[0]
        c = 1
        res = ""
        for i in word[1:]:
            if i !=s:
                res +=str(c)+s
                s = i
                c = 1
            else:
                c+=1
                if c>9:
                    res +="9"+s
                    c=1
        res += str(c) +s
        return res