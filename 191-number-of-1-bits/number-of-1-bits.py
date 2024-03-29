class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)
        print(temp)
        c = Counter(temp)
        print(c)
        return c['1']