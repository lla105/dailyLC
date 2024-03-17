# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        current = head
        prevnode = None

        reversehead = None
        while current:
            nextnode = current.next # 2,3
            current.next = prevnode # 1 -> None, 2->1

            prevnode = current # 1

            # print(current.next)
            reversehead = prevnode
            current = nextnode # 2




        # print(reversehead)
        return reversehead

