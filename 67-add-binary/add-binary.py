class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # print( bin(int(a)), bin(int(b)) )
        temp = int(int(a,2) + int(b,2))
        return bin(temp)[2:]

        return '1010'

        # 1 = 1
        # 2 = 10
        # 3 = 11
        # 4 = 100
        # 8 = 1000
        # 9 = 1001
        # 10 = 1010
        # 11 = 1011 
    