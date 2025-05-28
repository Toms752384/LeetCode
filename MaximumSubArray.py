from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force solution
        # initilize result
        max_sum = nums[0]

        for i in range(len(nums)):
            # initilize sum for the sub array starting from the i'th index
            cur_sum = 0
            for j in range(i, len(nums)):
                # compute the sum of the sub array starting from i till the end
                # of the array, and update along the way max value if found it 
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
                
        return max_sum
