class Solution:
    def maxProfit(self, prices: List[int], i=0, cache=None, holding=False) -> int:
        if cache is None:
            cache = {}
        state = (i, holding)
        if state in cache:
            return cache[state]
        
        if i >= len(prices):
            return 0
        if holding:
            sell = prices[i]
            hold = self.maxProfit(prices, i + 1, cache=cache, holding=True)
            res = max(sell, hold)
        else:
            buy = -prices[i] + self.maxProfit(prices, i + 1, cache=cache, holding=True)
            wait = self.maxProfit(prices, i + 1, cache=cache, holding=False)
            res = max(buy, wait)
        cache[state] = res
        return res
