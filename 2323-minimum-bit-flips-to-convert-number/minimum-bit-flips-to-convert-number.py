class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def inttobin(n):
            if n==0:
                return '0'
            arr = []
            while n>0:
                arr.append(str(n%2))
                n = n//2
            return ''.join(reversed(arr))

        startbin = str(inttobin(start))
        goalbin = str(inttobin(goal))
        # print(startbin, goalbin)
        m = len(startbin)
        n = len(goalbin)
        if m > n :
            diff = m-n
            zeros = []
            for i in range(diff):
                zeros.append('0')
            zerostring = ''.join(zeros)
            goalbin = zerostring + goalbin
        else:
            diff = n-m
            zeros = []
            for i in range(diff):
                zeros.append('0')
            zerostring = ''.join(zeros)
            startbin = zerostring + startbin
        # print(startbin, goalbin)
        count = 0
        for i in range(len(goalbin)):
            if startbin[i] != goalbin[i] :
                count +=1 
        return count