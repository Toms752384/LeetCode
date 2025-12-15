from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # naive - O(m*nlogn)
        # # initialize a dictionary
        # res = defaultdict(list)

        # # iterate through the strings
        # for s in strs:
        #     SortedS = sorted(s)
        #     res[SortedS].append(s)
         
        # return list(res.values())

        # improved algorithm - use the Valid anagram way
        # initalize dict
        res = defaultdict(list)

        # iterate through the strings
        for s in strs:
            # create a map for the string 's' to act as key
            s_key = {}  
            for i in range(len(s)):
                if s[i] in s_key:
                    s_key[s[i]] += 1
                else:
                    s_key[s[i]] = 1
            # add the string to the result map
            res[frozenset(s_key.items())].append(s) 
        return list(res.values())
    
def main():
    sol = Solution()
    strs=["ddddddddddg","dgggggggggg"]
    print(sol.groupAnagrams(strs))


if __name__ == "__main__":
    main()