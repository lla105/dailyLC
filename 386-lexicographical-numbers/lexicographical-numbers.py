class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(baseIndex):
            if baseIndex * 10 > n:
                return

            for i in range(baseIndex * 10, baseIndex * 10 + 10):
                if i > n:
                    break
                result.append(i)
                dfs(i)

        for i in range(1, 10):
            if i > n:
                break
            result.append(i)
            dfs(i)

        return result