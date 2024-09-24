class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1,arr2 = arr2, arr1

        print(' arr1 : ', arr1)
        print(' arr2 : ', arr2)
        set1 = set()
        for num in arr1:
            while num not in set1 and num != 0:
                set1.add(num)
                num = num//10
        set2 = set()
        max_prefix = 0
        for num in arr2:
            while num not in set1 and num!=0 :
                num = num //10
            if num != 0:
                max_prefix  = max(max_prefix , len(str(num)))
        print(' set1 : ', set1)
        return max_prefix