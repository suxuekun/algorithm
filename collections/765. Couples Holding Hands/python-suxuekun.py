class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n2 = len(row)
        n = n2//2

        for i in range(0,n2,2):
            row[i] //= 2
            row[i+1] //= 2


        rec = None
        for k in range(n):
            i = k+k
            while row[i] != k and row[i+1] != k:
                x = max(row[i],row[i+1])*2
                if x == rec:
                    x = min(row[i],row[i+1])*2
                rec = x
                row[x],row[x+1],row[i],row[i+1] = row[i],row[i+1],row[x],row[x+1]
        
        for k in range(n):
            i = k+k
            if row[i] != k:
                row[i],row[i+1] = row[i+1],row[i]
        

        count = 0
        for k in range(n):
            i = k+k+1
            while row[i] != k:
                x = row[i]*2 +1
                row[i],row[x] = row[x],row[i]
                count +=1
        
        return count
        

            
