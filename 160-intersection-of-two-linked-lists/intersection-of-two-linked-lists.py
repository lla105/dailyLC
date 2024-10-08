# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()

        curA = headA
        curB = headB
        while curA:
            if curA not in s:
                s.add(curA)
            curA = curA.next
        while curB:
            if curB in s:
                return curB
            else:
                s.add(curB)
            curB = curB.next
        return None