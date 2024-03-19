# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def printlist(somehead) :
    cur = somehead
    while cur : 
        print(f'{cur.val}->', end='')
        cur = cur.next
    print("\n=====")
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        h1 = head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        h2 = slow.next
        slow.next = None # tail 
        printlist(slow)
        
        # reverse slow (h2)
        prevnode = None
        revhead = None
        while h2:
            nextnode = h2.next
            h2.next = prevnode
            prevnode = h2
            revhead = h2
            h2 = nextnode
        printlist(h1)
        printlist(revhead)

        answerhead = h1
        h2 = revhead
        while h2:
            next1 = h1.next
            h1.next = h2
            next2 = h2.next
            h2.next = next1
            h1 = next1
            h2 = next2
        printlist(answerhead)

        return answerhead



