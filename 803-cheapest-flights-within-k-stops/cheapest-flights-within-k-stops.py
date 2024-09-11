class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list) # format : { source1:[ (dest,price), (dest2,pricer2) ]}
        for fromNode, toNode, price in flights:
            d[fromNode].append( (toNode, price) )
        bestPrices = [ float('inf') ] * n
        bestPrices[src] = 0
        # print(' best prices: ', bestPrices)
        # print( ' dict : ', d)

        q = deque()
        q.append( (src, 0 , 0) )

        while q:
            fromNode, curstops , prevcost = q.popleft()
            if curstops > k:
                continue
            neighborlist = d[fromNode]
            for nextNode, nextPrice in neighborlist:
                newPrice = nextPrice + prevcost
                if newPrice < bestPrices[nextNode]:
                    bestPrices[nextNode] = newPrice
                    q.append( (nextNode, curstops+1 , newPrice) )
        if bestPrices[dst]!= float('inf'):
            return bestPrices[dst]
        else:
            return -1