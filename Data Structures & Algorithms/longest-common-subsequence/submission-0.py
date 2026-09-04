class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str,i=0,j=0, memo = None) -> int:
        if memo is None: memo = {}
        pair = (i, j)
        if pair in memo: return memo[pair]
        if i == len(text1) or j == len(text2): return 0
        if text1[i] == text2[j]:
            res = 1 + self.longestCommonSubsequence(text1, text2, i+1, j+1, memo)
        else:
            res = max(self.longestCommonSubsequence(text1, text2, i+1, j, memo),
                        self.longestCommonSubsequence(text1, text2, i, j+1, memo))
        memo[pair] = res
        return memo[pair]