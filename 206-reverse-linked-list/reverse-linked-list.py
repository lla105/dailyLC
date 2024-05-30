# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answerhead = None
        previousnode = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = previousnode
            previousnode = cur
            cur = temp
            answerhead = previousnode
        return answerhead