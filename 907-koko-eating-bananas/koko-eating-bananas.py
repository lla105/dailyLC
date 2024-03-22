def countTotalTurns(piles, speed):
    turnsUsed = 0
    for i in range(len(piles)):
        turnsUsed += piles[i] // speed
        if piles[i] % speed != 0:
            turnsUsed += 1
    return turnsUsed

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxspeed = max(piles)
        piles = sorted(piles)
        left = 1
        right = maxspeed
        fastest = maxspeed

        while left <= right:
            mid = (left+right)//2
            turnsUsed = countTotalTurns(piles, mid)
            print(f'{left} ---- {mid} ---- {right}')
            print(f'[{mid}]: , TurnsUsed: {turnsUsed}')
            if turnsUsed > h :
                left = mid + 1
            else: # turnsUsed qualifies.
                fastest = min(fastest, mid)
                right = mid - 1
            print(f'fastest: {fastest}')
        return fastest
