class Solution:
    def appealSum(self, s: str) -> int:
        lastseendic = {}
        # dic format = { char : last seen index }
        ptotal=0
        ctotal = 0
        total = 0
        for i in range(len(s)):
            print(i)
            char = s[i]
            if char in lastseendic: # we've seen this char before
                ctotal = (i- lastseendic[char]) + ptotal
            else: # new char. never before seen
                ctotal = i + 1 + ptotal
            lastseendic[char] = i
            total += ctotal
            ptotal = ctotal
        return total



# s = abcd
# i
# 0:a      a>1 =1
# 1:ab     ab>2, b>1 =3
# 2:abc    abc>3, bc>2, c>1 = 6
# 3:abcc.  abcc>3, bcc>2, cc>1, c>1 =7
# 3:abcb.  abcb>3, bcb>2, cb>2, b>1 =8
# 3:abca.  abca>3, bca>3, ca>2, a>1 =9
# 3:abcd.  abcd>4, bcd>3, cd>2, d>1 =10 <-- all new letters



# if new char is not seen before:
#     (current index)+1 +(previous total)
# if new char is seen before:
#     (current index - previous seen index) +previous total

# update dictionary 
