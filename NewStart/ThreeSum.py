from typing import List


class Solution:
    # algorithm:
    # naive - do a triple for loop for each combination. when finds a combination, add it to the list of results
    # improved:
    # init a set
    # init two pointers
    # sort the list 
    # iterate in a while loop until l > r
    # inside the while loop iterate with i to check the target sum - 0
    # check if the indices are different
    # add to result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # improved
        res = set()
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                # update left or right - according to the value
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                
                # if found 3 sum, add to result
                else:
                    tmp = [nums[i], nums[l], nums[r]]
                    tmp.sort
                    res.add(tuple(tmp))
                    # move pointer 
                    l += 1
                    while nums[l] == nums[l-1] and l < r: # skip duplicates
                        l += 1

        return [list(i) for i in res]
    
        # # naive
        # res = set() # use a set to avoid dups
        # n = len(nums)
        # nums.sort() # sort to handle dups

        # # iterate on the list with i < j < k
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if (nums[i] + nums[j] + nums[k] == 0):
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))
        # return [list(i) for i in res]
        

def main():
    sol = Solution()
    nums=[-2,0,1,1,2]
    print(sol.threeSum(nums))

if __name__ == "__main__":
    main()