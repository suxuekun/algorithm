from math import factorial
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        arr = [int(c) for c in str(n)]
        @lru_cache(10 * 11)
        def factor(n, k):
            if k == 0:
                return 1
            return n * factor(n - 1, k - 1)
        seen = set()
        res = 0
        for i, d in enumerate(arr):
            t = sum(1 for j in range(0 if i > 0 else 1, d) if j not in seen)
            res += t * factor(10 - len(seen) - 1, len(arr) - i - 1)
            if d in seen:
                break
            seen.add(d)
        else:
            res += 1
        # print(res)
        for i in range(1, len(arr)):
            res += 9 * factor(9, len(arr) - i - 1)
        
        return res