# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        length = 0
        cur = head
        while cur:
            length+=1
            d[length] = cur
            cur = cur.next
        mid = (length//2)+1
        return d[mid]
