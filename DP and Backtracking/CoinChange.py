from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # recursive solution
        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     res = float('inf')
        #     for coin in coins:
        #         if coin <= amount:
        #             res = min(res, 1 + dfs(amount - coin))
        #     return res

        # res = dfs(amount)
        # return -1 if res >= float('inf') else res
    
        # DP with memozation:
        # DP with memozation:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = float('inf')
            for coin in coins:
                if coin <= amount:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res # store in memory
            return res

        res = dfs(amount)
        return -1 if res >= float('inf') else res