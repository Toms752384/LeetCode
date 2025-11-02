from typing import List


class Solution:
    # input: array of integers (could contain zero)
    # output: array of integers - where output[i] = products of all elements except nums[i]

    # first algorithm: calculate product using a loop, and save it
    # then, initialize an output array size of nums with 0's, and iterate on it - for
    # each one, check if nums[i] is 0. if so, calculate the product again without it, and store it
    # if not, divide the product by nums[i]
    # analysis: O(n^2) in the worst case - every element is zero

    # second algorithm: try to save repeted work in an array
    # initialize a data array size nums, and in it store the product of every element up until this point (not including)
    # then, initialize a reverse data array, same as the firt, but do it in reverse
    # then - initialize an output array which will contain: output[i] = data[i - 1] * data2[i + 1]
    # analysis: O(n) space and time

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # second algorithm
        # initialize the arrays
        length = len(nums)
        output = [0 for i in range(length)]
        data = [1 for i in range(length)]
        reverse_data = [1 for i in range(length)]

        # compute product up until the i'th place and store in the data array
        data[0] = 1
        product = nums[0]
        for i in range(1, length):
            data[i] = product
            product *= nums[i]
        
        # compute product in reverse
        reverse_data[length - 1] = 1
        product = nums[length - 1]
        temp = length - 2
        while(temp >= 0):
            reverse_data[temp] = product
            product *= nums[temp]
            temp -= 1

        # find the output using the data and reverse data arrays
        for i in range(length):
            output[i] = data[i] * reverse_data[i]

        return output
        # # first algorithm
        # # find product of entire array
        # product = 1
        # for num in nums:
        #     product *= num
        # length = len(nums)
        # output = [0 for i in range(length)]

        # # find output products
        # for i in range(length):
        #     if nums[i] != 0:
        #         output[i] = int (product / nums[i])
        #     else:
        #         new_product = 1
        #         for j in range(length):
        #             if i != j:
        #                 new_product *= nums[j]
        #         output[i] = new_product
        
        # return output

def main():
    sol = Solution()
    nums = [1,2,4,6]
    print(sol.productExceptSelf(nums))
    
if __name__ == "__main__":
    main()

