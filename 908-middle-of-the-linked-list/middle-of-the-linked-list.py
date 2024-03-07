# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length=0
        while current:
            length+=1
            current = current.next
        # print(f'length:{length}')
        # # print(f'dic: {dic}')
        # print(f'5//2={5//2}')
        # print(f'6//2={6//2}')
        current = head
        for i in range(length//2):
            current = current.next
        return current


