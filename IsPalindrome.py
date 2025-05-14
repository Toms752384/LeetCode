class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Algorithm: initialize a left and a right pointer to the string, and iterate until they point to the same index.
        If one of them points to a non - alphanumeric character, move it to the next character. compare each time, and if not
        identical, return false. use two helper function - is_non_alphanumeric and are_the_same_val"""
        # initialzie pointers
        left_pointer = 0
        right_pointer = (len(s) - 1)
        
        # iterate until pointers meet
        while left_pointer < right_pointer:  
            # check if left pointer is non alphanumeric
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue

            # check if right pointer is non alphanumeric
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue

            # check if character are the same
            if not self.are_same_val(s[left_pointer], s[right_pointer]):
                return False
            
            # advance both pointer for the next iteration
            left_pointer += 1
            right_pointer -= 1
                
        # if passed comparison, it's a palindrome
        return True
    
    def are_same_val(self, left, right) -> bool:
        """Checks if characters have the same alpanumeric value"""
        # if both are numbers
        if '0' <= left <= '9' and '0' <= right <= '9':
            return left == right
        
        # if both are characters
        if ('a' <= left <= 'z' or 'A' <= left <= 'Z') and ('a' <= right <= 'z' or 'A' <= right <= 'Z'):
            return left.lower() == right.lower()

        # if not the same range 
        return False
    
def main():
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome(""))                                # True
    print(sol.isPalindrome(" "))                               # True
    print(sol.isPalindrome("0P"))                              # False

if __name__ == "__main__":
    main()


