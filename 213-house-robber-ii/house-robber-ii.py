class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        cache1 = [0] * (len(nums)-1)
        cache2 = [0] * (len(nums)-1)
        # [200,3,140,20,10]
        cache1[0] = nums[0]
        cache1[1] = nums[1]
        cache1[2] = nums[0] + nums[2]
        # cache1 = [200,3,340,0]
        cache2[0] = nums[1]
        cache2[1] = nums[2]
        cache2[2] = nums[1] + nums[3]
        # cache2 = [3,140,23,0]
        print(cache1)
        print(cache2)
        # [200,3,140,20,10]
        for i in range(3 , len(cache1)) :
            cache1[i] = max( (cache1[i-2]+nums[i]) , (cache1[i-3]+nums[i]) )
            cache2[i] = max( (cache2[i-2]+nums[i+1]) , (cache2[i-3]+nums[i+1]) )
            print(cache1)
            print(cache2)
            print('=====')
        return max(cache1[-1], cache1[-2] , cache2[-1] , cache2[-2])

#nums=[a,b,c,d,e,f]
#cache1=[a,b,c,d,e]
#cache2=[b,c,d,e,f]

#[a,b,c,d,e,f,g]
#[a,b,c,d,e,f]
#[b,c,d,e,f,g]

# d+a, e+a, f+b
# if len(nums)>4