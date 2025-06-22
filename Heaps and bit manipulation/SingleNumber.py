from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Given an array of integers, where all elements appear twice and one appears once, return the one
        that appears only once - in O(1) space"""
        # algorithm: initialize a res value with the first number, traverse the array from the second element (add edge case for zero/one element)
        # and xor all elements on res. return the result of res
        
        # edge case - handle empty array
        if nums is None:
            return None
        
        res = nums[0]
        # second edge case - one element
        n = len(nums)
        if n == 1:
            return res
        
        # traverse the array and xor each element
        for i in range(1, n):
            res = res ^ nums[i]

        return res