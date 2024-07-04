class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = Counter(magazine)
        ranCount = Counter(ransomNote)
        for i,v in ranCount.items():
            # print(i,v)
            if i in magCount and v<=magCount[i]:
                pass
            else:
                return False

        return True