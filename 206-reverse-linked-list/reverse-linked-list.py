# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseHead = None
        prevNode = None
        cur = head
        while cur:
            tempnext = cur.next
            cur.next = prevNode
            prevNode = cur
            reverseHead = cur
            cur = tempnext
        return reverseHead
        