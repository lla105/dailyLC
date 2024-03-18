# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        s1 = []
        s2 = []

        while cur1:
            s1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            s2.append(cur2.val)
            cur2 = cur2.next
        temp1 = 0
        for i in range(len(s1)-1, -1, -1):
            temp1 *= 10
            temp1 += s1[i]
        # print(temp1)
        temp2 = 0
        for i in range(len(s2)-1, -1, -1):
            temp2 *= 10
            temp2 += s2[i]
        summ = temp1+temp2
        print(summ)
        ssum = str(summ)
        # print(len(ssum))
        resultlist = []

        dummy = ListNode()
        curr = dummy

        for i in range(len(ssum)-1, -1, -1):
            # print(ssum[i])
            curr.next = ListNode(int(ssum[i]))
            curr = curr.next

        return dummy.next