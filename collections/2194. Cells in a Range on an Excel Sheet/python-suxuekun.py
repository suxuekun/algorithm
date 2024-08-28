class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a,b = s[0],s[3]
        c,d = s[1],s[4]
        l1 = range(ord(a),ord(b)+1);
        l2 = range(int(c),int(d)+1);
        res = []
        
        for i in l1:
            for j in l2:
                item = chr(i) + str(j);
                res.append(item)
                
        return res
        
        