class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        maxlen = 0
        middleUsed = False

        for i,v in d.items():
            # aab -> aba
            # aabc --> a_a
            # aaac --> aca
            print(i,maxlen)
            if v%2==0: #v is even
                maxlen += v
            else: # v is odd
                # v is 1
                if v==1:
                    if middleUsed==False:
                        maxlen += 1
                else:
                    if middleUsed==False:
                        maxlen += v
                    else:
                        maxlen += v
                        maxlen -= 1
                print(i,v)
                # v is >1 odds, eg: 5

                middleUsed=True
            print(i,maxlen)
            
        return maxlen