# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # algorithm: init two pointers, one that moves one node at a time, and the second two nodes at a time. If one of the (probably 
    # the faster one) points to none, return false. Once if they point at the same node - return true
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # base case - empty list
        if head == None: 
            return False
        
        # base case - one node
        if head.next == None:
            return False
        
        # initialize two pointers
        slow = head
        fast = head.next

        # traverse list until one of the pointers points to none
        while fast != None:
            # if they point to the same node - cycle detected
            if slow == fast:
                return True
            
            # advance the pointers    
            slow = slow.next
            if fast.next == None: # fast pointer reached the end
                return False
            fast = fast.next
            if fast.next == None: # check for the second time
                return False
            fast = fast.next

        # if reached here one of them reached the end - return false
        return False
        