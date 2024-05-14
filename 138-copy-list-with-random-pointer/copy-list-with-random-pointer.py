
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None
        
        # Step 1: Create the new interleaved list
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next, None)
            curr.next = new_node
            curr = new_node.next
        
        # Step 2: Assign random pointers to the new nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the interleaved list into original and copied lists
        curr = head
        new_head = head.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            curr = curr.next
        
        return new_head