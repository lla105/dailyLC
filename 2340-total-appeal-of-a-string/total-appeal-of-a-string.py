class Solution:
    def appealSum(self, s: str) -> int:
        lastseendic = {}
        # lastseendic format = { char : last seen index }

        ctotal = 0
        ptotal = 0
        total = 0

        for i in range(len(s)):
            char = s[i]
            if char in lastseendic:
                ctotal = ptotal + (i - lastseendic[char])
            else:
                ctotal = i + 1 + ptotal
            lastseendic[char] = i
            total += ctotal
            ptotal = ctotal 
        return total 



# s: "abc"
# 0: a:     a>1 = 1
# 1: ab:    ab>2, b>1 = 3
# 2: abc:   abc>3, bc>2, c>1 = 6
# 3: abcd:  abcd>4, bcd>3, cd>2, d>1 = 10
# 3: abcc:  abcc>3, bcc>2, cc>1, c>1 = 7
# 3: abcb:  abcb>3, bcb>2, cb>2, b>1 = 8
# 3: abca:  abca>3, bca>3, ca>2, a>1 = 9

# # 4: abcde: abcde>5, bcde>4, cde>3, de>2, e>1. =15 

# if char is NOT seen before: 
#     current total = (current index) + 1 + previous total
#     all total = previous total + current total 

# if char is seen before:
#     current total = previous total + (how far previous index is)