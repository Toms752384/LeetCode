from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # handle base cases - empty list or one house
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return max(0, nums[0])
        
        # initialize an array size n+1 with zero's
        values = [0] * (n + 1)

        # populate the first and second elements in the array - zero and first element
        values[0], values[1] = 0, nums[0]

        # populate the array using the max check
        for i in range(2, n + 1):
            values[i] = max(values[i - 1], values[i - 2] + nums[i - 1])
        
        # return the last element
        return values[n]

def main():
    sol = Solution()
    houses = [2, 9, 8, 3, 6]
    print(sol.rob(houses))
    
if __name__ == "__main__":
    main()    