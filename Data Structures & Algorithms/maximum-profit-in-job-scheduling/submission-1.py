class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        n = len(startTime)
        memo = {}
        def dp(i):
            if i in memo: return memo[i]
            if i >= n: return 0
            j = i+1
            while j<n and jobs[i][1] > jobs[j][0]:
                j+=1
            profit1 = jobs[i][2] + dp(j)
            profit2 = dp(i+1)
            memo[i] = max(profit1, profit2)
            return memo[i]
        return dp(0)