class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        def trav( curList, index ) :
            # print('. curList : ', curList)
            # if len(curList) >= len(s):
            if index >= len(s): 
                self.result.append( tuple(curList) )

            for i in range( index, len(s)):
                s1 = s[index:i+1]
                s2 = []
                for j in range(len(s1)-1 , -1, -1):
                    s2.append(s1[j])
                s2 = ''.join(s2)
                # print( ' s1: ', s1 , ' vs ', s2)
                if s1==s2:
                    # print('  match!')
                    trav( curList+[s1] , i+1)

        trav([] , 0)
        return self.result