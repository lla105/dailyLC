# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        for num in nums:
            s.add(num)
        backptr = ListNode()
        frontptr = head
        backptr.next = frontptr
        answer = backptr
        
        while frontptr:
            if frontptr.val in s:
                backptr.next = frontptr.next
                frontptr = frontptr.next
            else:
                backptr = frontptr
                frontptr = frontptr.next
        return answer.next
    