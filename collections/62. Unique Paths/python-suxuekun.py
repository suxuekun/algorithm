class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        j = min(m,n)
        i = m+n-1
        if j ==1:
            return 1
        if i <3:
            return 1
        res = reduce(lambda x,y:x*y,range(i-j+1,i))
        res = res//reduce(lambda x,y:x*y,range(1,j))
       
        return res