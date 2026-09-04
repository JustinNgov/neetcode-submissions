class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            if rem in memo: return memo[rem]
            if rem == 0: return 0
            if rem < 0: return float('inf')
            
            min_coins = float('inf')
            
            for c in coins:
                res = 1 + dfs(rem - c)
                
                if res < min_coins:
                    min_coins = res
            
            memo[rem] = min_coins
            return min_coins

        result = dfs(amount)
        return result if result != float('inf') else -1