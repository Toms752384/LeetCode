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

def main():
    sol = Solution()
    text1 = ""
    text2 = ""
    print(sol.longestCommonSubsequence(text1, text2))

if __name__ == "__main__":
    main()   