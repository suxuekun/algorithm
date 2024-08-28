class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        h = {}
        c = 0
        for i in sentence:
            if not h.get(i):
                c+=1
                h[i] = 1
                if c==26:
                    return True
        return False

        