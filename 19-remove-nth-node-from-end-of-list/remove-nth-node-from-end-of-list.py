# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printlist(self, head):
        current = head
        while current:
            print(f'{current.val}', end='')
            if current.next:
                print(f'->',end='')
            current = current.next
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # self.printlist(head)
        dummy = ListNode(0)
        dummy.next = head
        # self.printlist(dummy)
        first = dummy
        second = dummy

        for i in range(n+1):
            second = second.next

        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        self.printlist(dummy.next)
        return dummy.next
