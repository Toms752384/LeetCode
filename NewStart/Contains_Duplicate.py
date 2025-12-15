from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Docstring for hasDuplicate
        algorithm: add the numbers to a set while checking if a value is already in place
        :param self: class
        :param nums: array of integers
        :type nums: List[int]
        :return: true if a value appears more than twice, false otherwise
        :rtype: bool
        """
        # add the numbers to a set with the value as key, and a counter as value
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
