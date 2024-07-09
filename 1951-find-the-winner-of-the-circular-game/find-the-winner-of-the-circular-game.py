class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        starting = 0
        for i in range(1, n+1):
            starting = (starting+k) % i
        return starting+1
