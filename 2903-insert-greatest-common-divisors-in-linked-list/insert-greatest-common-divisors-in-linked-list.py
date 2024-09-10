# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right = head
        left = head.next
        if not right:
            return None
        if not left:
            return head

        def getGCD(a,b):
            return math.gcd(a,b)

        while right and left:
            gcdval = getGCD(right.val, left.val)
            newnode = ListNode(gcdval, left)
            right.next = newnode
            right = left
            left = left.next
        return head