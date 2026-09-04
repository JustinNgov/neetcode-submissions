class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        table = [[False] * (m+1) for _ in range(n+1)]
        for j in range(m+1):
            table[0][j] = True
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = table[i][j-1]
        return table[n][m]