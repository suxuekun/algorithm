class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x;

        res = 1;
        s = x
        while n > 0:
            if (n &0x01):
                res *= s
            s *=s
            n >>= 1
        return res
                

        # s = [x]
        # i = 1
        # while i < n:
        #     s.append(s[-1]*s[-1])
        #     i = i<<1
        # m = n

        # c = 0;
        # res = 1
        # while m > 0:
        #     if (m & 0x01):
        #         res*=s[c]
        #     m >>=1
        #     c +=1

        # return res


            