class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        new_x = x
        y = 0
        while new_x > 0:
            remainder = new_x % 10
            y += remainder
            new_x //= 10
        z = x % y
        return y if z == 0 else -1
        