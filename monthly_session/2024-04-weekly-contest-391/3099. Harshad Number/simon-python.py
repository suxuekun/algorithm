class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def get_digit_sum(num):
            return sum([int(i) for i in str(num)])
        
        digit_sum = get_digit_sum(x)
        
        return digit_sum if x % digit_sum == 0 else -1