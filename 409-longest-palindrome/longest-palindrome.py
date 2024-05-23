class Solution:
    def longestPalindrome(self, s: str) -> int:
        usedsingle = False
        maxlen = 0
        d1 = Counter(s)
        for i,v in d1.items():
            print(i,v)
            if v%2==0:
                maxlen+=v
            elif v%2!=0: #is an odd number
                if v/2>=1:
                    maxlen+=v
                    maxlen-=1
                if usedsingle==False:
                    maxlen+=1
                    usedsingle = True
            print(maxlen)
        return maxlen