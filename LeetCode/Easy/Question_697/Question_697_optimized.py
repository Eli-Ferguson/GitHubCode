class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        d = defaultdict( list )
        
        degree, minSpan = 1, 1
        
        for i, n in enumerate( nums ) :

            d[ n ].append( i )
            count = len( d[ n ] )

            if count > degree :
                degree = count
                minSpan = i - d[ n ][ 0 ]
            
            elif count == degree :
                minSpan = min( minSpan, i - d[ n ][ 0 ] )

        return minSpan+1

nums = [1,2,2,3,1,4,2]

print( f'Min Sub Arr With Degree: {Solution.findShortestSubArray( super, nums )}' )

# Beats 53.84% Runtime, 239ms
# Beats 5.18% Memory, 17.8mb