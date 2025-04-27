class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_arr = []
        s2_arr = []
        match_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i] :
                s1_arr.append( s1[i] )
                s2_arr.append( s2[i] )
            else:
                match_count += 1
        # if s1_arr[0] == s2_arr[1] and s1_arr[]
        if match_count != len(s1)-2 and len(s1_arr)!=0 :
            return False

        if sorted(s1_arr) == sorted(s2_arr) :
            return True
        else:
            return False