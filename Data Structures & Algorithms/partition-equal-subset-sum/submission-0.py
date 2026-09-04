class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums) % 2 != 0: return False
        memo = {}
        def dp(i, remaining):
            if (i, remaining) in memo: return memo[(i, remaining)]
            if remaining == 0: return True
            if remaining < 0 or i == len(nums): return False
            include = dp(i+1, remaining - nums[i])
            exclude = dp(i+1, remaining)
            res = include or exclude
            memo[(i, remaining)] = res
            return res
        return dp(0, target)
        