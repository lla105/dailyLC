class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        self.output = []
        def isPalindrome( somestring ):
            l = 0
            r = len(somestring) - 1
            while l<r:
                if somestring[l] != somestring[r] :
                    return False
                l+=1
                r-=1
            return True
        def bf( curList , index ) :
            # if len(curList) == len(s):
                # return
            if index >= len(s):
                self.output.append( tuple(curList) )
                return
            for i in range( index , len(s) ):
                tempstring = s[index : i+1]
                temp = isPalindrome( tempstring )
                if temp:
                    bf( curList+[tempstring] , i+ 1 )
        bf( [] , 0 ) 
        return self.output