class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case - one row or one column
        if m == 1 or n == 1:
            return 1

        # initialize a matrix size m*n to help compute answer
        vals = [[0 for i in range(n)] for j in range(m)]
        
        # initialize the first row and first column with 1's
        for i in range(n):
            vals[0][i] = 1
        for j in range(m):
            vals[j][0] = 1
        
        # fill the rest of the array
        for i in range(1, m):
            for j in range(1, n):
                vals[i][j] = vals[i - 1][j] + vals[i][j - 1]

        return vals[m - 1][n - 1]

def main():
    sol = Solution()
    m, n = 3, 6
    # print(sol.uniquePaths(m, n))
    sol.uniquePaths(m, n)
    
if __name__ == "__main__":
    main()   