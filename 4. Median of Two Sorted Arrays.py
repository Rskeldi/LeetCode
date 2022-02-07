class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a = [*nums1, *nums2]
        a.sort()
        if len(a) % 2 == 0:
            num1 = int(len(a) / 2)
            return sum(a[num1-1:num1+1]) / 2
        else:
            return a[len(a) // 2]
