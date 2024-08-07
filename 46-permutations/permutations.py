class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        resultlist = []

        def trav( curList , alist ):
            if len(curList)>=len(nums):
                resultlist.append(curList)
                return
            
            for i in range(len(alist)):
                nextalist = alist[:i] + alist[i+1:]
                trav( curList+[alist[i]] , nextalist )

        trav( [] , nums )
        return resultlist
