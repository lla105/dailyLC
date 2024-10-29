from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = {}  # Memoization dictionary to store results of each cell
        
        def trav(i, j):
            # If the result for this cell is already computed, return it
            if (i, j) in memo:
                return memo[(i, j)]
            
            cur_val = grid[i][j]
            max_distance = 0
            # Define the three directions: (up-right), (right), (down-right)
            directions = [(i-1, j+1), (i, j+1), (i+1, j+1)]
            
            for dx, dy in directions:
                # Check boundaries and increasing condition
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] > cur_val:
                    max_distance = max(max_distance, 1 + trav(dx, dy))
            
            memo[(i, j)] = max_distance  # Store the result for this cell
            return max_distance
        
        # Initialize max moves
        max_moves = 0
        # Start from the first column for each row
        for i in range(n):
            max_moves = max(max_moves, trav(i, 0))
        
        return max_moves
