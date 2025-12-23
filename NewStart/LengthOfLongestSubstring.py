class Solution:
    # naive algorithm: for each index in the string, check the longest consecutive substring without repeating characters, by
    # initializing an empty temp set, and adding to it until a non - unique char is added
    # improved algorithm: use the sliding window algorithm:
    # edge case - if empty or single char
    # init l and r pointers
    # init res = 1
    # init an empty temp set
    # add l to the set
    # iterate until r reaches the end of the string:
        # if s[r] isn't in the set: add it, and expand the window by one. also update: res++
        # if s[r] is in the set: remove s[l] from the set, add s[r] to the set and advance the window by one forward 
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle edge cases
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # initalize variables
        l, r = 0, 1
        res = temp = 1
        window = set()
        window.add(s[l])

        # iterate through the string
        while(r < n):
            if s[r] not in window:
                window.add(s[r])
                r += 1
                temp += 1
            else: 
                # update res if needed 
                res = max(res, temp)
                while l < r:
                    if s[r] in window:
                        window.remove(s[l])
                        l += 1
                    else:
                        break
                window.add(s[r])
                r += 1
                temp = r - l # update temp window length
        
        res = max(res, temp)
        return res


def main():
    sol = Solution()
    s="asgshdrr"
    print(sol.lengthOfLongestSubstring(s))
    
if __name__ == "__main__":
    main()