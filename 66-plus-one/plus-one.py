class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1]+1
        for i in range(len(digits)-1, -1, -1):
            print(i)
            if digits[i]==10 and i==0:
                # print("a", digits[i])

                digits.insert(0,1)
                digits[1] = 0
                # print("a", digits[1])

            elif digits[i]==10:
                digits[i] = 0
                # print("b: ", digits[i])
                digits[i-1] = digits[i-1] + 1
        return digits
        
        # [6,7,8,9]
        # [6,7,9,0]


        # [9,9,9]
        # [0,0,0]
        # [1,0,0,0]

        # templist = [1,2,3]
        # templist.insert(0,7)
        # print(templist)
