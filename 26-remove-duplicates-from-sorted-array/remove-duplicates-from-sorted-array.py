class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # print(nums)
        answer = 0
        ss = set()
        temparray = []
        for i in range(len(nums)):
            if nums[i] not in ss:
                ss.add(nums[i])
                temparray.append(nums[i])
        print(temparray)

        for i in range(len(temparray)):
            answer+=1
            nums[i] = temparray[i]
        
        # for i in range(len(nums)):
        #     if nums[i] in ss:
        #         nums[i:len(nums)-i] = nums[i+1:]
        #         print(nums)
        #     else:
        #         answer+=1
        #         ss.add(nums[i])
        return answer
