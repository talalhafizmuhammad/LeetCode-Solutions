class Solution(object):
    def sumOfEncryptedInt(self, nums):
        sum = 0
        for i in nums:
            digits = list(str(i))
            max_digit = max(digits)
            encrypt = int(max_digit * len(digits))
            sum += encrypt
        return sum
