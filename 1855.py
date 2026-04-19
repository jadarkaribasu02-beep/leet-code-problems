#1855. Maximum Distance Between a Pair of Values

#You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

#A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

#Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

#An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

class Solution:
    def maxDistance(self, nums1, nums2):
        i, j = 0, 0 # i = nums1 and j = nums2
        k_jadar = 0
        
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # Valid pair -> update max distance
                k_jadar = max(k_jadar, j - i)
                j += 1  # move j forward to try for larger distance
            else:
                i += 1  # nums1[i] too large, move i forward
        
        return k_jadar # k_jadar = maxdist
