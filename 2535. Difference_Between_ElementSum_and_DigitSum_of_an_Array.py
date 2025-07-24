class Solution(object):
    def differenceOfSum(self, nums):
        el_sum = 0
        dig_sum = 0
        for i in range(len(nums)):
            el_sum += nums[i]
        dig_sum = sum(int(d) for num in nums for d in str(num))
        return abs(el_sum - dig_sum)


        
