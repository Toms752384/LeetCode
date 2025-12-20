from typing import List


class Solution:
    # naive algorithm: for each day, compute the best day to sell it on and the profit from it
    # by maintaing a max_profit variable - O(n^2)
    # improved: use sliding window algorithm
    # init max to 0 and left and right pointers to the start of the list
    # start advancing the window:
        # compute profit
        # if negative, advance the window: l = r, r++
        # if positive, update max if needed and expand window: r++
        # continue until r reaches the end

    def maxProfit(self, prices: List[int]) -> int:
        # edge case - empty list
        if prices is None:
            return 0
        
        # initialize variables
        max_profit = 0
        l, r = 0, 1
        n = len(prices)

        while(l < r and r < n):
            current_profit = prices[r] - prices[l]
            if current_profit < 0:
                l = r
                r += 1
                continue
            max_profit = max(max_profit, current_profit)
            r += 1

        return max_profit
        
def main():
    sol = Solution()
    prices = [10,8,7,5,2]
    print(sol.maxProfit(prices))
    
if __name__ == "__main__":
    main()