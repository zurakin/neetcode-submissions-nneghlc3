class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1, right1 = 0, len(nums1) - 1
        left2, right2 = 0, len(nums2) - 1

        while left1 <= right1 and left2 <= right2:
            mid1 = (left1 + right1) / 2
            mid1Value = nums1[int(mid1)] if mid1.is_integer() else (nums1[int(mid1)] + nums1[int(mid1) + 1]) / 2

            mid2 = (left2 + right2) / 2
            mid2Value = nums2[int(mid2)] if mid2.is_integer() else (nums2[int(mid2)] + nums2[int(mid2) + 1]) / 2

            if mid1Value == mid2Value:
                return mid1Value

            if mid1Value < mid2Value:
                left1 = int(mid1) + 1
                right2 = math.ceil(mid2) - 1
            else:
                left2 = int(mid2) + 1
                right1 = math.ceil(mid1) - 1
        
        if left1 <= right1:
            return median(nums1[left1: right1+1])
        if left2 <= right2:
            return median(nums2[left2: right2+1])
        return (mid1Value + mid2Value) / 2

def median(arr):
    med = (len(arr)-1) / 2 
    if med.is_integer():
        return arr[int(med)]
    return (arr[int(med)] + arr[int(med) + 1]) / 2