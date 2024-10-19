class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def flip(text):
            if text=='0':
                return '1'
            else:
                return '0'
        def rev_inv(string):
            output = ''
            for i in range(len(string)-1,-1,-1):
                output += str( flip(string[i] ))
            return output
        prev = '0'
        for i in range(n-1):
            s1 = prev
            s2 = '1'
            s3 = rev_inv(prev)
            prev = s1+s2+s3
        # temp = rev_inv('0111001')
        # print(prev)

        return prev[k-1]