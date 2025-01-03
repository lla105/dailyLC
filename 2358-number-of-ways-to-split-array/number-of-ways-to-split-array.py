class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        stack = [ nums[0] ]
        q = deque()
        splits = 0
        for i in range(1,len(nums)):
            q.append( nums[i] )
        print(stack)
        print(q)
        stacksum = sum(stack)
        qsum = sum(q)
        print(stacksum)
        print(qsum)
        if stacksum >= qsum:
            splits += 1
        for i in range( 1 , len(nums)-1 ):
            rm_num = q.popleft()
            qsum -= rm_num
            stack.append( rm_num )
            stacksum += rm_num
            if stacksum >= qsum:
                # print(' good : ', stack, ' vs ', q)
                splits += 1
        return splits
