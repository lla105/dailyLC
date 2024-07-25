class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr , level ):
            # if level >9:
            #     return arr
            if len(arr)==2:
                # print(level*'-', 'Reached bottom2: ', arr)
                if arr[0]>arr[1]:
                    arr[1],arr[0] = arr[0], arr[1]
                return arr
            elif len(arr)==1:
                # print(level*'-', 'Reached bottom1: ', arr)
                return arr
            left = mergesort(arr[ : len(arr)//2] , level+1)
            right = mergesort(arr[ len(arr)//2 : ] , level+1)
            # print(level*'-', ' returned Left : ', left)
            # print(level*'-', ' returned Right : ', right)
            i = 0
            j = 0
            mergedArray = []
            while i<len(left) and j<len(right):
                if left[i] > right[j]:
                    mergedArray.append(right[j])
                    j+=1
                else:
                    mergedArray.append(left[i])
                    i+=1
            while i<len(left):
                mergedArray.append(left[i])
                i+=1
            while j<len(right):
                mergedArray.append(right[j])
                j+=1
            # print(level*'-', ' mergedArray : ', mergedArray)
            return mergedArray
        
        return mergesort(nums, 0)
