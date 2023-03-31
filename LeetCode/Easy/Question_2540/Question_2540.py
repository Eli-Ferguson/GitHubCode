class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2) :
            
            if nums1[i] == nums2[j] :  return nums1[i]
            elif nums1[i] > nums2[j] : j += 1
            else : i += 1
        
        return -1

# Beats 49.75% Runtime, 473ms
# Beats 93.57% Memory, 32.3mb