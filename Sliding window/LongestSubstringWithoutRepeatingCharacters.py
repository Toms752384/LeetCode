# input: string s
# output: length of longest substring without duplicates in the string
# brute force algorithm: iterate through each suffix and use a set to find the length of the longest substring starting from that. return the index with the
# largest counter - O(n^2) time, O(n) space. 
# improved algorithm: use two pointer - left and right. left will be the index of the start of the substring, and right will be its ending.
# start when both are zero, and iterate using "right" on the string, all the while adding letters to the substring, and counting.
# each time finds a dup, store in a max variable, remove the character that "left" is pointing at, and increase "left" by one - moving the pointer to the next character.
# stop iterating when "right" reaches the end  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # improved algorithm
        # initialize variables
        left = right = 0
        seen = set()
        max_length = 0
        n = len(s)

        # handle edge case 
        if n == 0:
            return max_length
        
        # iterate through the string
        current_length = 0
        while(left <= right and right < n):
            if s[right] in seen: # if found a dup
                seen.remove(s[left])
                left += 1
                current_length -= 1
                continue

            seen.add(s[right])
            current_length += 1
            max_length = max(max_length, current_length)
            right += 1

        return max_length

        # # brute force
        # # initalize variables
        # n = len(s)
        # counters = [0 for i in range(n)]

        # # handle edge case
        # if n == 0:
        #     return 0
        
        # # iterate through the string to find the largest index
        # for i in range(n):
        #     current_counter = 0
        #     current_set = set()
        #     for j in range(i, n):
        #         if s[j] in current_set:
        #             break
        #         current_counter += 1
        #         current_set.add(s[j])
        #     counters[i] = current_counter

        # return max(counters)

        
def main():
    sol = Solution()
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()
        
        