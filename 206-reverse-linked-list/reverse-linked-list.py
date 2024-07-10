# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevnode = None
        newhead = None
        cur = head

        while cur:
            tempnext = cur.next
            cur.next = prevnode
            prevnode = cur
            newhead = cur
            cur = tempnext

        return newhead