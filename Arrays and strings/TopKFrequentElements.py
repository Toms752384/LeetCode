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
        # initalize variables
        res = []
        counters = {}

        # iterate through the list to count the frequencies
        for num in nums:
            if num in counters:
                counters[num] += 1
            else:
                counters[num] = 1
        
        # find the top k elements in the dictinary
        for _ in range(k):
            max_key = max(counters, key=counters.get)
            res.append(max_key)
            counters.pop(max_key)

        return res