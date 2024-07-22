# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        mid = (length//2)+1
        cur = head
        i = 0
        while i+1<mid:
            cur = cur.next
            i+=1
        return cur
