from typing import List


class Solution:
    # naive algorithm: for each bar check against all the rest - (r - l) * min(h[r], h[l])
    # improved algorithm - use two pointers
    # init two pointers - left and right
    # init max_area variable to 1
    # iterate with the two pointers and compute the area
    # move the pointer with the smaller height
    # return the result
     
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        l, r = 0, n - 1

        while(l < r):
            current_area = (r - l) * min(heights[r], heights[l])
            max_area = max(max_area, current_area)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_area
def main():
    sol = Solution()
    heights = [1,7,2,5,4,7,3,6]
    print(sol.maxArea(heights))
    
if __name__ == "__main__":
    main()