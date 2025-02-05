class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        mismatch_index = []
        for i in range(len(s1)):
            if s1[i] != s2[i] :
                mismatch_index.append(i)
        # s1_new = 
        if len(mismatch_index) >2:
            return False
        print(mismatch_index)

        if len(mismatch_index) == 2:
            a = mismatch_index[0]
            b = mismatch_index[1]
            # s1_new = s1[:mismatch_index[0]] + s2[mismatch_index[0]] + s1[mismatch_index[0]+1 : mismatch_index[1]] + s2[mismatch_index[1]] + s1[mismatch_index[1]+1 :]
            s1_new = s1[:a] + s1[b] + s1[a+1:b] + s1[a] + s1[b+1:] 
        elif len(mismatch_index) == 1:
            return False
        print(f's1_new : {s1_new}')
        if s1_new == s2:
            return True
        else:
            return False