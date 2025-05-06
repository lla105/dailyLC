class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        def isPalindrome( arr ) :
            i = 0
            j = len(arr) - 1
            while i<j and arr[i]==arr[j] :
                i+=1
                j-=1
            if i == j or i-1==j :
                return True
            else:
                return False
        def trav( cur_list , idx):
            if idx == len(s):
                output.append( tuple(cur_list) )
                return
            for i in range( idx, len(s) ):
                ispalin = isPalindrome(s[idx:i+1])
                if ispalin:
                    trav( cur_list+[ s[idx:i+1]], i+1 )
            return
        trav( [], 0 )
        return output
            # aba
            # aa