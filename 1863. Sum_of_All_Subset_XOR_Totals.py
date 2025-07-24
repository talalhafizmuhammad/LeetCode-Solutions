class Solution(object):
    def subsetXORSum(self, nums):
        
        def dfs(i, current_xor):
            if i == len(nums):
                return current_xor
            return dfs(i+1, current_xor ^ nums[i]) + dfs(i+1, current_xor)
        
        return dfs(0, 0)
