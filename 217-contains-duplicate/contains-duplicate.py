class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        heheset = set() 
        for num in nums:
            if num in heheset : 
                return True
            else:
                heheset.add(num)
        return False 