class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = word1, word2
        m, n = len(w1), len(w2)

        # cache[i][j] = min distance from w2[i:] to w1[j:]
        cache = [[-1] * (m + 1) for _ in range(n + 1)]

        def trav(i, j):
            if i == n:  # exhausted w2 → insert remaining w1[j:]
                return m - j
            if j == m:  # exhausted w1 → delete remaining w2[i:]
                return n - i
            if cache[i][j] != -1:
                return cache[i][j]
            if w1[j] == w2[i]:
                cache[i][j] = trav(i + 1, j + 1)
            else:
                insert = trav(i + 1, j)
                delete = trav(i, j + 1)
                replace = trav(i + 1, j + 1)
                cache[i][j] = 1 + min(insert, delete, replace)
            return cache[i][j]

        return trav(0, 0)
