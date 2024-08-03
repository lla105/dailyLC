class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sum(target) != sum(arr):
            return False
        tdic = Counter(target)
        adic = Counter(arr)
        for num in target:
            if tdic.get(num) != adic.get(num):
                return False
        return True