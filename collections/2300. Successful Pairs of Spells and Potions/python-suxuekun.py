class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(spells)
        n = len(potions);
        res = [0]*m
        
        for i in range(m):
            score = success / spells[i];
            j = n//2;
            s,e = 0,n;
            while True:
                potion = potions[j]
                if potion < score:
                    s = j+1
                else:
                    e = j
                if s == e:
                    break;
                j = (e+s)//2;
            res[i] = n-s;
        return res