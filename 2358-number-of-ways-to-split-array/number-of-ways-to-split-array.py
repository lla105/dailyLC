class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # stack = [ nums[0] ]
        # q = deque()
        qsum = 0
        splits = 0
        stacksum = nums[0]
        for i in range(1,len(nums)):
            # q.append( nums[i] )
            qsum += nums[i]
        # stacksum = sum(stack)
        if stacksum >= qsum:
            splits += 1
        for i in range( 1 , len(nums)-1 ):
            # rm_num = q.popleft()
            rm_num = nums[i]
            qsum -= rm_num
            # stack.append( rm_num )
            stacksum += rm_num
            if stacksum >= qsum:
                splits += 1
        return splits
