class Solution:
    def tribonacci(self, n: int, cache=None) -> int:
        if cache is None: cache = {}
        if n in cache: return cache[n]
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        res = self.tribonacci(n-3, cache) + self.tribonacci(n-2, cache) + self.tribonacci(n-1, cache)
        cache[n] = res
        return res