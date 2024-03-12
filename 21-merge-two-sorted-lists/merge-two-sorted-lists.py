# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printlist(self,head):
        current = head
        while current:
            print(f'{current.val}',end='')
            if current.next:
                print(f'->',end='')
            current = current.next
        print("")
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode()
        current = dummyhead

        while list1 and list2:
            if list1.val >= list2.val:
                print(f'append list2: {list2.val}')
                current.next = list2
                list2 = list2.next
            else:
                print(f'append list1: {list1.val}')
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        self.printlist(dummyhead.next)
        return dummyhead.next