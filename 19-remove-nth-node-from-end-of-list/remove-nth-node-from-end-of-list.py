# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def printlist(somelist):
            cur = somelist
            print( ' printing list')
            while cur:
                print(cur.val, end='->')
                cur = cur.next 
            print()
        if not head.next:
            return None
        slow = ListNode(99)
        returnhead = slow
        slow.next = head
        fast = slow.next
        count = 0
        while fast and count<n:
            count+=1
            fast = fast.next
        printlist(slow)
        printlist(fast)
        while fast:
            fast = fast.next
            slow = slow.next
        # print(slow)
        # print(slow.next)
        # print()
        # print(fast)
        print()
        printlist(slow)
        printlist(fast)

        temp = slow.next
        slow.next = temp.next


        return returnhead.next