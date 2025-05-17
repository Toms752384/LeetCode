from typing import List
# Naive algorithm: traverse the list to find the mininal solution
# improved algorithm: use binary search. the desired number is smaller from both it's sides
# Initialize two pointers - left and right, for the ends of the array.
# check the element is (l + r) / 2.  
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init two pointers
        left, right = 0, len(nums) - 1

        # do special binary search
        while(left < right):
            mid = int((left + right) / 2)

            # update pointers
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 

        return nums[left]
        
        # naive algorithm
        # res = 0
        # for num in nums:
        #     res = min(res, num)
        # return res 
def main():
    sol = Solution()
    nums=[3,4,5,6,1,2]
    print(sol.findMin(nums))
    
if __name__ == "__main__":
    main()