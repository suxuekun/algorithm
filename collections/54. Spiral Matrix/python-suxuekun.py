class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []

        n = len(matrix)

        m = len(matrix[0])

        i = 0
        j = m-1

        p = 0
        q = n-1

        while i<j and p<q:
            res += matrix[p][i:j+1]
            
            for k in range(p+1,q):
                res.append(matrix[k][j])
            res += matrix[q][i:j+1][::-1]

            for k in range(q-1,p,-1):
                res.append(matrix[k][i])
            i+=1
            j-=1
            p+=1
            q-=1
        if i == j:
            if p == q:
                res.append(matrix[p][i])
            elif p<q:
                for k in range(p,q+1):
                    res.append(matrix[k][i])
        elif i<j:
            if p == q:
                for k in range(i,j+1):
                    res.append(matrix[p][k])




        return res