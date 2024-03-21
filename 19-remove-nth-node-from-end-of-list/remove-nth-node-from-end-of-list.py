# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def printlist(head):
    cur = head
    while cur:
        print(f'{cur.val}->', end='')
        cur = cur.next
    print("")
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        h1 = dummy
        h2 = dummy
        dummy.next = head
        
        # printlist(h1)
        for i in range(n+1):
            h2 = h2.next
        # printlist(h1)
        # printlist(h2)
        while h2:
            h1 = h1.next
            h2 = h2.next
        # printlist(h1)
        # printlist(h2)
        h1.next = h1.next.next

        return dummy.next