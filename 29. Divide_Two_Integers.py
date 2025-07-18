class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        quotient = abs(dividend) // abs(divisor)
        
        if (dividend < 0) ^ (divisor < 0):
            return -quotient
        else:
            return quotient
