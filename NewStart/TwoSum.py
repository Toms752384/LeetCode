from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Docstring for twoSum
        :param self: solution class
        :param nums: array of integers
        :type nums: List[int]
        :param target: target sum 
        :type target: int
        :return: list of two indices that their sum is the target
        :rtype: List[int]
        """
        # map nums to a hash map
        hashmap = {}

        # iterate through the array and check sums
        for index, value  in enumerate(nums):
            if (target - value) in hashmap:
                return [hashmap[target - value], index]
            hashmap[value] = index

        return []

def main():
    sol = Solution()
    nums=[3, 4, 5, 6]
    print(sol.twoSum(nums, 7))
    
if __name__ == "__main__":
    main()