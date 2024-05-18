class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1 and nums[0]==target:
            return [0,0]

        def binarysearch(searchingLeft):
            left = 0
            right = len(nums)-1
            tempindex = -1
            while left<=right :
                # mid = (left+right)//2 
                # mid += left
                mid = left + (right-left) // 2
                print('  ', left,mid,right)
                print('. ', nums[left], nums[mid], nums[right])
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    tempindex = mid
                    if searchingLeft == True:
                        right = mid - 1
                    else:
                        left = mid + 1
            return tempindex

        L = binarysearch(True)
        R = binarysearch(False)

        return [L,R]
