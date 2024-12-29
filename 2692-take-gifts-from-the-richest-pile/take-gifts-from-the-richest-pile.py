class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n_gifts = []
        for i in range(len(gifts)):
            n_gifts.append( -1*gifts[i] )
        heapq.heapify(n_gifts)
        # print(n_gifts)
        for _ in range(k):
            rm_num = heapq.heappop(n_gifts)
            rm_num = -1 * rm_num
            rm_num = sqrt(rm_num)
            heapq.heappush( n_gifts, int((-1*rm_num)) )
            # print(n_gifts)
        return sum(n_gifts)*-1