from typing import List


class Solution:
    # Improved algorithm: two pointers: initialize left and right pointers to the first and second elements.
    # if the left element is smaller, check the profit and update max if needed. if not, advance left pointer to right element, and each iteration advance right pointer.
    def maxProfit(self, prices: List[int]) -> int:
        # initialize variables
        maxP = 0
        l, r = 0, 1

        # iterate through the array
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

    
        # brute force
        # diff = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         temp = prices[j] - prices[i]
        #         diff = max(diff, temp)
        # return diff

def main():
    sol = Solution()
    prices=[5,1,5,6,7,1,10]
    print(sol.maxProfit(prices))
    
if __name__ == "__main__":
    main()