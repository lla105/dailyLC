class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        arr = []
        while i<len(nums1) and j<len(nums2) and len(arr)< (((len(nums1)) + len(nums2))//2)+1:
            if nums1[i] > nums2[j] :
                arr.append(nums2[j])
                j+=1
            else:
                arr.append(nums1[i])
                i+=1
        while i<len(nums1):
            arr.append(nums1[i])
            i+=1
        while j<len(nums2):
            arr.append(nums2[j])
            j+=1

        if len(arr)%2==0:
            m1 = arr[len(arr)//2]
            m2 = arr[ (len(arr)//2) - 1]
            return (m1+m2)/2
        else:
            return arr[len(arr)//2]