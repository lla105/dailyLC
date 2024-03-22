class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1]+1
        for i in range(len(digits)-1, -1, -1):
            print(i)
            if digits[i]==10 and i==0:
                digits.insert(0,1)
                digits[1] = 0
            elif digits[i]==10:
                digits[i] = 0
                digits[i-1] = digits[i-1] + 1
        return digits
        
