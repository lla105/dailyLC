class Solution:
    def makeFancyString(self, s: str) -> str:
        d = {}
        newstring = []
        for i in range(len(s)):
            if i<2:
                newstring.append(s[i])
                continue
            if s[i] == s[i-1] == s[i-2] :
                continue
            newstring.append(s[i])
            # freq = d.get( s[i] , 0 ) 
            # if i<2:
            #     if freq+1 >= 3:
            #         continue
            #     else:
            #         newstring.append(s[i])
            #         d[s[i]] = freq+1
            #         continue
            # if freq+1 == 3:
            #     continue
            # d[s[i-2]] -= 1
            # d[s[i]] = freq+1
            # newstring.append(s[i])
            # print(i, newstring, d)



        return ''.join(newstring)