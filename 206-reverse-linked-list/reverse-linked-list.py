# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prevnode = None
        rhead = None

        while cur :
            nextnode = cur.next
            cur.next = prevnode
            prevnode = cur
            cur = nextnode

        return prevnode 