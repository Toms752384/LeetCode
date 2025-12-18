from typing import List


class Solution:
    # naive - compute each element in a double loop - for each element compute the product of all the others  - O(n^2)
    # imporved with division: 
    # if two or more zeros - return all zeros
    # if one zero - compute the product without it, apply it to the index with the zero and reutrn 0 in all other elements
    # no zeros - use division
    # improved without division - compute two lists - prefixes and suffixes lists
    # the prefix list holds in each element the product of all those before it, and the suffix the product of all those before it
    # find all of them and compute the result with ease by multiplying the corrosponding elements from each list
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefixes = [1] * n
        suffixes = [1] * n

        # compute the prefixes
        prefix_product = nums[0]
        for i in range(1, n):
            prefixes[i] = prefix_product
            prefix_product *= nums[i]
        
        print(prefixes)
        
        # compute the suffixes
        suffix_product = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffixes[i] = suffix_product
            suffix_product *= nums[i]

        print(suffixes)
        
        # compute result
        for i in range(n):
            res[i] = prefixes[i] * suffixes[i]
        
        return res


        # # with division
        # # initialize variables
        # n = len(nums)
        # res = [0] * n
        # counter = 0
        
        # # count number of zeros
        # for num in nums:
        #     if num == 0:
        #         counter += 1
        
        # # if found two or more
        # if counter >= 2: 
        #     return res

        # # handle one or no 0's    
        # total_product = 1
        # total_product_without_zero_index = 1
        # zero_index = None

        # # find total product
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         zero_index = i
        #         total_product *= num
        #     else:
        #         total_product *= num
        #         total_product_without_zero_index *= num
        
        #  # if found zero
        # if zero_index != None:
        #     res[zero_index] = total_product_without_zero_index

        # else:
        #     for i, num in enumerate(nums):
        #         res[i] = int(total_product / num)

        # return res


def main():
    sol = Solution()
    nums = [1, 2, 4, 6]  
    print(sol.productExceptSelf(nums))


if __name__ == "__main__":
    main()