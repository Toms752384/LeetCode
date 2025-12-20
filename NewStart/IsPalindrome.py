class Solution:
    # algorithm:
    # initalize left and right pointers
    # start iterating on them by comparing the value of the chars they point to
    # ignore non alphanumerical characthers - use a helper function

    def isPalindrome(self, s: str) -> bool:
        # init variables
        n = len(s)
        l, r = 0, n - 1

        # iterate the string
        while(l < r):
            # check if the characters are alphanumerical
            if not (s[l].isalpha() or s[l].isdigit()):
                l += 1
                continue
            elif not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
                continue
            
            # compare the values
            if s[l].lower() != s[r].lower():
                return False
            
            # advance the pointers
            l += 1
            r -= 1
        return True
    

def main():
    sol = Solution()
    s="Never odd or even"
    print(sol.isPalindrome(s))


if __name__ == "__main__":
    main()