from typing import List
# input: array of integers and a positive k 
# output: top k most frequent elements in the array
# algorithm: use a hashmap to count the elements - {number: frequencies}. then find the max frequencies, k times
# analysis: O(n * k) runtime, O(n) space.
# improved algorithm: use bucket sort - initalize a list of empty lists - each inner list will hold the elements which have frequencies same as the list's index
# count using a hashmap, and add them to the list.
# use the buckets to append k elements to the result   
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # improved algorithm:
        # initalize variables
        res = []
        counters = {}
        buckets = [[] for i in range(len(nums) + 1)]

        # iterate through the list to count the frequencies
        for num in nums:
            if num in counters:
                counters[num] += 1
            else:
                counters[num] = 1
        
        # use the counters to add elements to the buckets
        for key in counters:
            buckets[counters[key]].append(key)
        
        # return the top k elements using the buckets
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        # # first algorithm:
        # # initalize variables
        # res = []
        # counters = {}

        # # iterate through the list to count the frequencies
        # for num in nums:
        #     if num in counters:
        #         counters[num] += 1
        #     else:
        #         counters[num] = 1
        
        # # find the top k elements in the dictinary
        # for _ in range(k):
        #     max_key = max(counters, key=counters.get)
        #     res.append(max_key)
        #     counters.pop(max_key)

        # return res


def main():
    sol = Solution()
    nums = [1,2,2,3,3,3,4,4,4] 
    k = 1
    print(sol.topKFrequent(nums, k))
    
if __name__ == "__main__":
    main()