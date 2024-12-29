class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxnum = float('-inf')
        for _ in range(k):
            maxnum = float('-inf')
            maxindex = -1
            for i in range(len(gifts)):
                if gifts[i] > maxnum :
                    maxindex = i
                    maxnum = gifts[i]
            gifts[maxindex] = int(sqrt(gifts[maxindex]))
            # print('>>> ', gifts)
        return sum(gifts)