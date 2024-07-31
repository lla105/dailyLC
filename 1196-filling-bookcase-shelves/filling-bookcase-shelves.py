class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            
            width = 0
            maxHeight = 0
            minHeight = float('inf')
            
            for j in range(i, n):
                width += books[j][0]
                if width > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                minHeight = min(minHeight, maxHeight + dfs(j + 1))
            
            memo[i] = minHeight
            return minHeight
        
        return dfs(0)