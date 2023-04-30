class Solution:
    def rob(self, nums: list[int]) -> int:

        # Check Base Cases
        ln = len( nums )
        if ln == 1 : return nums[ 0 ]
        elif ln == 2 : return max( nums[ 0 ], nums[ 1 ] )
        elif ln == 3 : return max( nums[ 0 ] + nums[ 2 ], nums[ 1 ] )

        # Dynamic Algorithm Array
        dp = [ 0 ] * ln

        # Fill in base cases
        dp[ 0 ] = nums[ 0 ]
        dp[ 1 ] = nums[ 1 ]
        dp[ 2 ] = max( nums[ 0 ] + nums[ 2 ], nums[ 1 ] )

        # Iterate through the rest of nums
        for i in range( 3, ln ) :

            dp [ i ] = max(
                dp[ i-2 ] + nums[ i ], # Skip i-1
                dp[ i-1 ], # Pick i-1
                dp[ i-3 ] + nums[ i ], # Skip i-1 and 1-2
            )
        
        # algorithm must end on either the last or second to last
        return max( dp[ -1 ], dp[ -2 ] )

nums = [2,7,9,3,1]

print( f'Most robbed without adjacent houses: {Solution.rob( super, nums )}' )
    
# Beats 22.62% Runtime, 38ms
# Beats 5.23% Memory, 16.3mb