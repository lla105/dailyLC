# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revhead = None
        newNext = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = newNext
            newNext = cur
            revhead = cur
            cur = temp
        print(revhead)
        return revhead