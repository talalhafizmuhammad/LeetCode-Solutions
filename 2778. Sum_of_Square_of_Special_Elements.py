class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        sum = 0
        for i in range(1, n+1):
            if i != 0:
                if n % i == 0:
                    sum += nums[i - 1]**2
        return sum
        
