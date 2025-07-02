class Solution(object):
    def minPathSum(self, grid):
        """
        Algorithm: use dynamic programming
        Recursive:
            base case:
            step:   
        :type grid: List[List[int]]
        :rtype: int
        """
        # # recursive solution
        # def dfs(n, m): # define helper function
        #     if n == len(grid) - 1 and m == len(grid[0]) - 1: # if reached bottom right corner - goal, return its vallue
        #         return grid[n][m]
        #     if n == len(grid) or m == len(grid[0]): # if slipped out of bounds, return infinity - so it won't be chosen
        #         return float('inf')
        #     return grid[n][m] + min(dfs(n + 1, m), dfs(n, m + 1)) # develope recursively - current value + minimun value of going right or goind down

        # return dfs(0, 0) # start from the top left corner 

        # dynamic programming solution
        # initalize an n*m array with 0's
        n = len(grid)
        m = len(grid[0])
        
        dp = [[0 for j in range(m)] 
                 for i in range(n)]

        # fill the array's first column and first row with the sum of its values until the current cell - only option to reach it
        dp[0][0] = grid[0][0]
        for i in range(1, n): # fill the first column
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for i in range(1, m): # fill the first row
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        # fill the array using the current value of cell and min between upper cell and right cell (options to reach that cell)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[n - 1][m - 1]
        
def main():
    sol = Solution()
    grid = [[2,2],[1,0]]
    print(sol.minPathSum(grid))

if __name__ == "__main__":
    main()
        
        
        