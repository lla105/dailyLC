class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1check = [0]*26
        # print(s1check)
        chardict = { 'a' : 0 ,
                    'b' : 1 ,
                    'c' : 2 ,
                    'd' : 3 ,
                    'e' : 4 ,
                    'f' : 5 ,
                    'g' : 6 ,
                    'h' : 7 ,
                    'i' : 8 ,
                    'j' : 9 ,
                    'k' : 10 ,
                    'l' : 11 ,
                    'm' : 12 ,
                    'n' : 13 ,
                    'o' : 14 ,
                    'p' : 15 ,
                    'q' : 16 ,
                    'r' : 17 ,
                    's' : 18 ,
                    't' : 19 ,
                    'u' : 20 ,
                    'v' : 21 ,
                    'w' : 22 ,
                    'x' : 23 ,
                    'y' : 24 ,
                    'z' : 25 ,
                    }
        d1 = {}
        d2 = {}
        for i in range(len(s1)):
            d1[s1[i]] = d1.get( s1[i] , 0) +1
            d2[s2[i]] = d2.get( s2[i] , 0) + 1
        if d1==d2:
            return True
        for i in range( len(s1) , len(s2) ):
            d2[s2[i-len(s1)]] = d2.get( s2[i-len(s1)] , 0 ) - 1
            d2[s2[i]] = d2.get( s2[i] , 0 ) + 1
            print(d2)
            count = 0
            for i,v in d1.items():
                if d2.get( i , 0 ) == v:
                    count += v
            if count == len(s1):
                return True

        return False