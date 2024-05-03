def CountUp(num, s) :
    count = 0
    while num in s:
        count+=1
        num+=1
    return count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        s = set()
        for num in nums:
            s.add(num)
        print(s)
        for num in nums:
            if num-1 not in s:
                seq = CountUp(num , s)
                answer= max(seq, answer)
            print(answer)
        return answer
            