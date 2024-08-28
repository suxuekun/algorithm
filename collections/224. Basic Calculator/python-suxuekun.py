class Solution:
    def calculate(self, s: str) -> int:

        total, num, sign, ans = 0, 0, 1, [1]

        for i in s + "+":
            if i.isdigit():
                num = num*10 + int(i)
            elif i in "+-":
                total += num*sign*ans[-1]
                sign = 1 if i == "+" else -1
                num = 0
            elif i == "(":
                ans.append(sign*ans[-1])
                sign = 1
            elif i == ")":
                total += num*sign*ans[-1]
                num = 0
                ans.pop()

        return total