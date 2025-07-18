class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = int(str(x_abs)[::-1])  

        result = sign * reversed_num

        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
