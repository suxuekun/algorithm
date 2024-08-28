class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = len(matrix);
        p = [0 for _ in matrix]
        
        j = 0
        while j<k:
            mi = 0
            m = None;
            for i in range(l):
                if p[i] >= len(matrix[i]):
                    continue
                e = matrix[i][p[i]]
                if m == None or e < m:
                    mi = i;
                    m = e;
            p[mi]+=1
            j +=1
        return m
            