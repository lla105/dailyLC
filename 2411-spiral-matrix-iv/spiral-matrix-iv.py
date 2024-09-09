class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the grid with -1
        grid = [[-1] * n for _ in range(m)]
        
        # Direction vectors: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_dir = 0  # Start moving right
        
        i, j = 0, 0  # Starting position
        while head:
            grid[i][j] = head.val
            head = head.next
            
            # Compute the next position
            next_i, next_j = i + directions[current_dir][0], j + directions[current_dir][1]
            
            # Check if the next position is out of bounds or already filled
            if not (0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == -1):
                # Change direction (right -> down -> left -> up -> right ...)
                current_dir = (current_dir + 1) % 4
                next_i, next_j = i + directions[current_dir][0], j + directions[current_dir][1]
            
            # Move to the next position
            i, j = next_i, next_j
        
        return grid
