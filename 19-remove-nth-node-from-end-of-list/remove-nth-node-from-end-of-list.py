# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def printlist(somehead):
    
    cur = somehead
    while cur : 
        print(f'{cur.val}->', end='')
        cur = cur.next
    print("\n=======")
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None :
            return head.next
        # if head.next.next == None and n==2:
        #     answerhead = head.next
            
        #     return answerhead

        
        cur = ListNode(0)
        h1 = cur
        cur.next = head
        for i in range(n):
            cur = cur.next
        temp = h1

        prev = None
        while cur : 
            prev = h1
            h1 = h1.next
            cur = cur.next
        # print(">>>>", h1.val)
        # h1.next = h1.next.next
        prev.next = prev.next.next
    
        printlist(temp)

        return temp.next
   