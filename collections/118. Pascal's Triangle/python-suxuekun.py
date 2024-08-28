class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==0:
            return [];
        res = [[1],[1,1]]
        if numRows < 3:
            return res[:numRows]
        for i in range(3,numRows+1):
            list=[1]*i
            if i%2==0:
                x = range(1,i//2)
            else:
                x = range(1,i//2+1)
            for j in x:
                list[j] = list[i-j-1] = res[i-2][j-1]+res[i-2][j]
            res.append(list)
        return res
    