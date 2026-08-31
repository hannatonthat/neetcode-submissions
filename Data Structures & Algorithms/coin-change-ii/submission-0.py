class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[-1] * (amount + 1) for i in range(len(coins))]

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if dp[i][a] != -1:
                return dp[i][a]
            
            res = 0
            if a >= coins[i]:
                res = dfs(i + 1, a)
                res += dfs(i, a - coins[i])
            dp[i][a] = res
            return res
        
        return dfs(0, amount)