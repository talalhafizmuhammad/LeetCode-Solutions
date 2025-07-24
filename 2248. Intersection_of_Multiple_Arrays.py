class Solution(object):
    def intersection(self, nums):
        if not nums:
            return []

        result = set(nums[0])
        for lst in nums[1:]:
            result &= set(lst)

        return sorted(list(result))
