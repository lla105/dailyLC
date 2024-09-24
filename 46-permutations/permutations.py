class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        def bf( curList , candidates ) :
            if len(curList) == len(nums) :
                output.append( tuple(curList ) )
                return
            for i in range( len (candidates) ):
                nextList = curList+[candidates[i]]
                firsthalf = candidates[:i]
                secondhalf= candidates[i+1:]
                nextcand = firsthalf + secondhalf
                bf( nextList , nextcand)
        bf( [] , nums )
        return output