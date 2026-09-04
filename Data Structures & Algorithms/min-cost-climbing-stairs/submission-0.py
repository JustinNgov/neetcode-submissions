class Solution:
    def minCostClimbingStairs(self, cost: List[int], i=0, cache = None) -> int:
        if cache is None:
            cache = {}
        if i in cache:
            return cache[i]
        if i >= len(cost):
            return 0 
        res = cost[i] + min(self.helper(cost, i+1, i, cache),
                            self.helper(cost, i+2, i, cache))
        cache[i] = res
        return res
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i in memo: return memo[i]
            if i >= len(cost): return 0
            res = cost[i] + min(dp(i+1), dp(i+2))
            memo[i] = res
            return res
            
        return min(dp(0), dp(1))