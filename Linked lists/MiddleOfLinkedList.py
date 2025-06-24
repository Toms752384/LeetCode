# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # algorithm: find length of the linked list by traversing it until the end
        # then, traverse it until the middle
        
        # find middle
        len = 0
        cur = head
        while(cur):
            len += 1
            cur = cur.next
        mid = int(len / 2)
        
        # traverse the list until the middle
        cur = head
        for _ in range(mid):
            cur = cur.next

        return cur 