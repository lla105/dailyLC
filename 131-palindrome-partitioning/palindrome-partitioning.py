class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        def isPalindrome( somestring ) :
            s1 = somestring
            s2 = []
            for j in range(len(s1)-1, -1, -1):
                s2.append(s1[j])
            s2 = ''.join(s2)
            return s1==s2
            
        def trav( curList, index) :
            if index >= len(s):
                self.result.append( tuple(curList) )
            for i in range( index, len(s) ):
                temp = isPalindrome( s[index:i+1] )
                # print(temp)
                if temp:
                    trav( curList+[s[index:i+1]] , i+1 )
        trav( [] , 0 )
        return self.result