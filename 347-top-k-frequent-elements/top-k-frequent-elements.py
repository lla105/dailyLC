class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        d = {}
        for num in nums :
            d[num] = d.get( num, 0 ) + 1
        d2 = {}
        # for num,freq in d.items():
        #     if freq in d2:
        #         d2[freq].append( num )
        #     else:
        #         d2[freq] = [ num ]
        # print(d)
        # print(d2)
        for num,freq in d.items() :
            heapq.heappush( h , (-freq,num) )
        # print(h)
        output = []
        while len(output) < k :
            temp = heapq.heappop(h)[1]
            output.append( temp )
        
        return output