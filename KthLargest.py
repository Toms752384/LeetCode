from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:
    # algorithm: create two attribute variables - k and heap, and all elements in nums to the heap.
    # initialize a min heap and add a minus to all elements to simulate a max heap
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        heapify(self.max_heap)
        for num in nums:
            heappush(self.max_heap, -num)
    
    # algorithm: use the heap to remove k elements, store them in a list, and when reaches k, store it in a variable,
    # put back elements inside the original heap and return the kth element
    def add(self, val: int) -> int:
        # add val to heap
        heappush(self.max_heap, val)

        # remove k elements from heap while appending to list
        temp = []
        res = 0
        for _ in range(1, self.k):
            res = heappop(self.max_heap)
            temp.append(res)
        
        # return elements back to heap
        for num in temp:
            heappush(self.max_heap, num)

        return (-res)
