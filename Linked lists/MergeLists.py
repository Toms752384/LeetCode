# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# naive algorithm: merge first list to second list, and sort
# improved algorithm:
# 1. compare the first elements of each list to decide who will be the head.
# 2. init head be the smaller head. cur1 = smaller_head.next, cur2 = head of list 2. also temp1 and temp2. also init cur = head
# 3. traverse both lists and until cur = None
# 4. each iteration, check if cur1.val < cur2.val. If so, then cur.next = cur1.next. else, temp = cur2.next, make 
# return head
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init pointers
        head = None
        cur1 = list1
        cur2 = list2

        # check edge cases
        if not cur1 and not cur2: # if both are empty
            return cur1
        elif not cur1: # if first list is empty
            return cur2
        elif not cur2: # if second list is empty
            return cur1

        # compare both heads to find minimal
        if cur1.val < cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        
        # traverse both lists
        cur = head
        while cur != None:
            # check if one of the lists is empty
            if not cur1:
                cur.next = cur2
                break
            elif not cur2:
                cur.next = cur1
                break

            # compare values
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        return head

def main():
    sol = Solution()
    list1, list2 = [1,2,4], [1,3,5]
    print(sol.mergeTwoLists(list1, list2)) #Output: [1,1,2,3,4,5]
    
if __name__ == "__main__":
    main()