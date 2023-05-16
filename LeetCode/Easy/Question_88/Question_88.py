class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1L = 0

        while n1L < ( len( nums1 ) - n ) and len( nums2 ) :

            if nums1[ n1L ] > nums2[ 0 ] :
                nums1.insert( n1L, nums2.pop( 0 ) )
                nums1.pop( -1 )
                n -= 1
            
            n1L += 1

        while nums2 :
            nums1[ n1L ] = nums2.pop( 0 )
            n1L += 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print( f'Merged Lists: {Solution.merge( super, nums1, m, nums2, n )}' )

# Beats 84.49% Runtime, 35ms
# Beats 9.55% Memory, 16.5mb