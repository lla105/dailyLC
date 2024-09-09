# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = []
        for i in range(m):
            row = [ -1 ] * n
            grid.append(row)
        def printgrid( somegrid):
            for i in range(len(somegrid)):
                for j in range(len(somegrid[0])):
                    print(somegrid[i][j], end=' ')
                print()
        # printgrid( grid)

        i=0
        j=0
        visited = set()
        while head:
            # right 
            while j<n and (i,j) not in visited and head:
                grid[i][j] = head.val
                head = head.next
                visited.add( (i,j) )
                j+=1
            j-=1
            i+=1
            # down
            while i<m and (i,j) not in visited and head:
                grid[i][j] = head.val
                head = head.next
                visited.add( (i,j) )
                i+=1
            i-=1
            j-=1
            #left
            while j>=0 and (i,j) not in visited and head:
                grid[i][j] = head.val
                head = head.next
                visited.add( (i,j) )
                j-=1
            j+=1
            i-=1
            # up 
            while i>=0 and (i,j) not in visited and head:
                grid[i][j] = head.val
                head = head.next
                visited.add( (i,j) )
                i-=1
            i+=1 
            j+=1
        return grid

        return grid