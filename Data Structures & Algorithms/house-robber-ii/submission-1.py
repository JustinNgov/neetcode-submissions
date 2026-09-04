class Solution:
    def rob(self, nums: List[int], i=0, cache=None) -> int:
        if len(nums) == 1: return nums[0]
        def rob_linear(houses: List[int]) -> int:
            memo = {}
            def helper(i):
                if i in memo: return memo[i]
                if i >= len(houses): return 0
                result = max(houses[i] + helper(i+2), helper(i+1))
                memo[i] = result
                return result
            return helper(0)
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))