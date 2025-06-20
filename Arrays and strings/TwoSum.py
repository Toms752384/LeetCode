
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """compute each element into a hashmap - dictionary, and then traverse the array to check for target - List[i]"""
    hashMap = {}
    for i, num in enumerate(nums):
        if target - num in hashMap:
            return [hashMap[target - nums[i]], i]
        hashMap[num] = i
    return []

def main():
    nums = [1, 2, 3, 4, 5]
    print(twoSum(nums, 5))
    
if (__name__ == "__main__"):
    main()
        

        

