class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        total_len = len(nums1) + len(nums2)
        median_pos = total_len // 2
        
        # Merge arrays only until we reach the middle point
        while i < len(nums1) and j < len(nums2) and len(merged) <= median_pos:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Append remaining elements from nums1 if needed, only until median position
        while i < len(nums1) and len(merged) <= median_pos:
            merged.append(nums1[i])
            i += 1
        
        # Append remaining elements from nums2 if needed, only until median position
        while j < len(nums2) and len(merged) <= median_pos:
            merged.append(nums2[j])
            j += 1
        
        # If total length is odd, return the middle element
        if total_len % 2 == 1:
            return merged[median_pos]
        else:
            # If total length is even, return the average of the two middle elements
            return (merged[median_pos] + merged[median_pos - 1]) / 2
