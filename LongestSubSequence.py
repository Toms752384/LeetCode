class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recursion first
        # # find lengths of both of the strings - n, m
        # n, m = len(text1), len(text2) 
        # # base case - one of the strings is empty
        # if n == 0 or m == 0:
        #     return 0

        # # check if the first characters are the same
        # if text1[0] == text2[0]:
        #     return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        
        # # if not, return the maximum value between removing the first char from the first
        # # string or from the second
        # return max(self.longestCommonSubsequence(text1[1:], text2),
        #             self.longestCommonSubsequence(text1, text2[1:]))
        
        # dynamic programming
        # Initialize a 2D DP array with dimensions (len(text1)+1) x (len(text2)+1)
        # All values are initially set to 0
        # dp[i][j] will hold the length of the longest common subsequence (LCS)
        # between text1[i:] and text2[j:]
        dp = [[0 for j in range(len(text2) + 1)] 
                 for i in range(len(text1) + 1)]

        # Fill the DP table in a bottom-up manner
        # Iterate from the end of each string towards the beginning
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # If characters match, increment LCS length by 1
                    # and use the value from the diagonally next cell
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If characters do not match, take the maximum
                    # between skipping a character from text1 or from text2
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # The result is stored in dp[0][0], representing the LCS length
        # between the full text1 and text2
        return dp[0][0]


def main():
    sol = Solution()
    text1 = ""
    text2 = ""
    print(sol.longestCommonSubsequence(text1, text2))

if __name__ == "__main__":
    main()   