from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: # find a possible start of a sequence 
                length = 1
                while (num + length) in numSet: # use the set to find the rest of the sequence 
                    length += 1
                longest = max(length, longest)
        return longest
    

def main():
    sol = Solution()
    nums=[2,20,4,10,3,4,5]
    print(sol.longestConsecutive(nums))


if __name__ == "__main__":
    main()