class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,1,1,2,2,2,3]
        if not nums:
            return []
        # if len(nums)==1:
        #     return [nums[-1]]
        d = Counter(nums) # format : { num:frequency }
 
        freqDict = {} # format : { freq: [num1, num2, ...] }
        # freqDict = {defaultdict(list)}
        for i,v in d.items():
            if v in freqDict:
                freqDict[v].append(i)
            else:
                freqDict[v] = [i]
            
        print(d)
        print(freqDict)

        result = []
        for i in range(len(nums), -1, -1):
            # print(i)
            if i in freqDict and k>0:
                j=0
                for j in range(len(freqDict[i])):
                    k-=1
                    result.append(freqDict[i][j])


        return result