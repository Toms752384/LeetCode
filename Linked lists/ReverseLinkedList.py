# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a linked list and returns the new head.
        Use a cur, prev and temp pointer to traverse the linked list - each time, advance the prev pointer to cur
        and then advance the cur pointer, while using the temp to point the next pointer to the one before it

        Args:
            head - pointer to a linked list

        Returns:
            head of the new linked list
        """
        prev = None
        cur = head
        while(cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev