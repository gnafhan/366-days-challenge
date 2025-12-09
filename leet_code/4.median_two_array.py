class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = sorted(nums1 + nums2)
        if len(array)%2 == 1:
            return array[int(len(array)/2)]
        return float((array[(len(array)/2)] + array[(len(array)/2)-1]))/2
    
    