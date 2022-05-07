# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

class Solution(object):
    def divide(self, dividend, divisor):
        def align_limits(quotient):
            positive_limit = 2 ** 31 - 1
            negative_limit = -2 ** 31

            if quotient < negative_limit:
                quotient = negative_limit
            elif quotient > positive_limit:
                quotient = positive_limit

            return quotient

        sign = -1 if ((dividend ^ divisor) < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend == 0:
            return 0
        elif divisor == 1:
            return align_limits(sign * abs(dividend))
        elif dividend == divisor:
            return sign * 1
        elif dividend < divisor:
            return 0

        quotient = 0
        power = 1
        original_divisor = divisor

        while dividend >= divisor:
            divisor = original_divisor ** power

            if power == 1:
                quotient += 1
                dividend -= divisor

            if power >= 2 and divisor > dividend:
                quotient += (original_divisor ** (power - 2))
                dividend -= (original_divisor ** (power - 1))
                divisor = original_divisor
                power = 0

            power += 1

        return -quotient if sign == -1 else quotient