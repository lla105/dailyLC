class Solution:
    def findComplement(self, num: int) -> int:
        def itob(somenum):
            binary = ''
            while somenum>0:
                remain = somenum%2
                binary = str(remain) + binary
                somenum = somenum//2
            return binary

        if num==0:
            return 1
        binnum = itob(num)
        print('binnum: ', binnum)
        flipped = []
        for num in binnum:
            if num=='1':
                flipped.append('0')
            else:
                flipped.append('1')
        flipped = ''.join(flipped)
        flipped = str(int(flipped))
        print(flipped)
        result = 0
        for i in range(len(flipped)):
            bit = int(flipped[i])
            result = result*2 + bit  
        return result