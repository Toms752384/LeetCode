from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Receives an input of n integers from [0, n] without dups and returns the integer that is missing"""
        # improved algorithm O(1) space: sum all the numbers from 0 to n (handle 0 as edge case?) then, traverse the list and subrtract
        # the list's values fro, the sum. return the sum - it will be the missing number
        # initialize
        n = len(nums)
        sum = 0
        for i in range(n + 1):
            sum += i
        
        # traverse the list and subtract the values
        for i in range(n):
            sum -= nums[i]

        return sum
        
        # naive algorithm - O(n) space: initialize a dictionary with integers from 0 - length of array with counter of 1 as value, and traverse the input
        # list - return the integer with the counter 1
        # initialize dict
        values = {}
        n = len(nums)

        # add values to dictionary
        for i in range(0, n + 1):
            values[i] = 1

        # traverse the list and add to counters
        for i in range(n):
            values[nums[i]] += 1

        # find the number with counter = 1
        res = 0
        for i in range(0, n + 1):
            if values[i] == 1:
                res = i
        
        return res