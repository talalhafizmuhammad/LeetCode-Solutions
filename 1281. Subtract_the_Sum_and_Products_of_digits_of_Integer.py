
class Solution(object):
    def subtractProductAndSum(self, n):
        a = 0
        p, s =1, 0
        while n > 0:
            a = n % 10
            s += a
            p *= a
            n //= 10
        return p - s
