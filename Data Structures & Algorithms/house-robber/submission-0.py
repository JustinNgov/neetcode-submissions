class Solution:
    def rob(self, nums: List[int], i=0, cache=None) -> int:
        if cache is None: cache = {}
        if i in cache: return cache[i]
        if len(nums) <= i:
            return 0
        result = max(nums[i] + self.rob(nums, i+2, cache), self.rob(nums, i+1, cache))
        cache[i] = result
        return result