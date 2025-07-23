class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeros], nums[i] = nums[i], nums[nonZeros]

                nonZeros += 1
