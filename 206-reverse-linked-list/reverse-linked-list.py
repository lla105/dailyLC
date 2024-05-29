# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversehead = None
        previousnode = None
        cur = head

        while cur:
            tempnextnode = cur.next
            cur.next = previousnode
            previousnode = cur 
            cur = tempnextnode
            reversehead = previousnode
        return reversehead