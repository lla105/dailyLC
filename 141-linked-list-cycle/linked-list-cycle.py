# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head 
        ss = set()
        while cur:
            print(f'{cur.val}->', end='')
            if cur in ss:
                return True
            else:
                ss.add(cur)
            cur = cur.next
        return False
