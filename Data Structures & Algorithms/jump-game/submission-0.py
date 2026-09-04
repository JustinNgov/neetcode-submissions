class Solution:
    def canJump(self, nums: List[int], i=0, memo = None) -> bool:
        if memo is None: memo = {}
        if i in memo: return memo[i]
        if i >= len(nums) - 1: return True
        max_jump = nums[i]
        for jump in range(max_jump, 0, -1):
            if self.canJump(nums, i+jump, memo):
                memo[i] = True
                return True
        memo[i] = False
        return False

