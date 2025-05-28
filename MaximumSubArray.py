from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # optimal solution
        # initialize variables and array of sums
        max_sum = nums[0]
        n = len(nums)
        sums = [0] * n

        # find the max sub array starting with the first index
        sum_for_first_index = nums[0]
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            sum_for_first_index = max(sum_for_first_index, cur_sum)
        sums[0] = sum_for_first_index
        
        # handle base case - only 1 element
        if n == 1:
            return max_sum

        # fill the rest of the array using the result of the first value
        max_sum = max(max_sum, sums[0])
        for i in range(1, n - 1):
            # compute the sum taking the max sum without the element from before
            temp = sums[i - 1] - nums[i - 1]
            if temp == 0:
                sums[i] = nums[i]
            else:
                sums[i] = sums[i - 1] - nums[i - 1]  
            max_sum = max(max_sum, sums[i])

        # fill the last element with the number from the nums array, and also check for max
        sums[n - 1] = nums[n - 1]
        max_sum = max(max_sum, sums[n - 1])

        # return the maximum value
        return max_sum
    
        # # brute force solution with O(1) memory
        # # initilize result
        # max_sum = nums[0]

        # for i in range(len(nums)):
        #     # initilize sum for the sub array starting from the i'th index
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         # compute the sum of the sub array starting from i till the end
        #         # of the array, and update along the way max value if found it 
        #         cur_sum += nums[j]
        #         max_sum = max(max_sum, cur_sum)

        # return max_sum
        # # brute force with O(n) memory
        # # compute the sums 
        # res = nums[0]
        # n = len(nums)
        # sums = [0] * n
        # for i in range(n):
        #     max_index_sum = nums[i]
        #     mid_sum = nums[i]
        #     for j in range(i + 1, n):
        #         mid_sum += nums[j]
        #         max_index_sum = max(max_index_sum, mid_sum)
        #     sums[i] = max_index_sum
                
        # print(sums)
        # # return the max sums
        # for temp in sums:
        #     res = max(temp, res)
        # return res
        
def main():
    sol = Solution()
    nums = [-2, -3, -1]
    print(sol.maxSubArray(nums))

if __name__ == "__main__":
    main()   