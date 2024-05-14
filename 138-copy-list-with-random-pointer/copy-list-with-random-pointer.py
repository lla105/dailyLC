class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        d = {}
        curr = head
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            d[curr].next = d.get(curr.next)
            d[curr].random = d.get(curr.random)
            curr = curr.next
        return d[head]
            