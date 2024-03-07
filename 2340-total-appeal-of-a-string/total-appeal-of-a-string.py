class Solution:
    def appealSum(self, s: str) -> int:
        lastseenmap = {}
        prev,curr,res = 0,0,0
        for i in range(len(s)):
            char = s[i]
            if char in lastseenmap:
                x = prev + ( i + 1)
                curr = x - (lastseenmap[char] +1)
                # curr = prev + ( i - lastseenmap[char])
            else:
                curr = prev + ( i + 1)
            res+=curr
            prev=curr
            lastseenmap[char] = i

        return res
                
            

# s = abcdb
# 0: a:    a>1 = 1
# 1: ab:   ab>2 , b>1 = 3
# 2: abc:  abc>3 , bc>2 , c>1 = 6
# 3:
# # abca: abca>3, bca>3, ca>2 , a>1 = 9 = 10 - index 0 + 1
# # abcb: abcb>3, bcb>2, cb>2 , b>1 = 8 = 10 - index 1 + 1
# # abcc: abcc>3, bcc>2, cc>1 , c>1 = 7 = 10 - index 2 + 1
# abcd: abcd>4, bcd>3, cd>2, d>1 = 10
# # abcdb:abcdb>4, bcdb>3, cdb>3, db>2, b>1

# observation1:
# if char is seen before, new count = x - (last seen index) + 1
# if char is not seen before, get x = (current index)+1 + previous total







        # lastSeenMap = {s[0]: 0}
        # prev, curr, res = 1, 0, 1
        
        # for i in range(1, len(s)):
        #     print("s[i]:", s[i], " ----> map:", lastSeenMap)
        #     if s[i] in lastSeenMap:

        #         curr = prev + (i - lastSeenMap[s[i]])
        #     else:
        #         curr = prev + (i + 1)
        #     print(f"curr:{curr}")
        #     res += curr
        #     prev = curr
        #     lastSeenMap[s[i]] = i
        #     print(lastSeenMap, " - res:", res)
        # return res