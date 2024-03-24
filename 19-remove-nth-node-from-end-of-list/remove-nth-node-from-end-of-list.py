# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def printlist(node):
    cur = node
    while cur:
        print(f'{cur.val}->', end='')
        cur = cur.next
    print("")
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        h1 = dummy
        h2 = dummy
        # printlist(h1)
        for i in range(n+1):
            h2 = h2.next
        while h2:
            h2 = h2.next
            h1 = h1.next
        h1.next = h1.next.next
        return dummy.next