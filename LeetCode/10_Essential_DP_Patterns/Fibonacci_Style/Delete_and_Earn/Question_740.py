from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        
        ln = len( nums )
        if ln == 1 : return nums[ 0 ]

        # Create list of nums representing the sum of their appearances in list nums
        c = Counter( nums )
        sums = [ 0 ] * ( max( c.keys() ) + 1 )
        for key in c.keys() : sums[ key ] = c[ key ] * key
        
        # initialize dp array
        dp = [ 0 ] * len( sums )
        dp[ 1 ] = sums[ 1 ]

        for i in range( 2, len( dp ) ) :
            
            dp[ i ] = max(
                dp[ i-1 ], # Pick i-1
                dp[ i-2 ] + sums[ i ], # skip i-1
            )
        
        return max( dp[ -1 ], dp[ -2 ] )

nums = [2,2,3,3,3,4]

print( f'delete and earn max: {Solution.deleteAndEarn( super, nums )}' )

# Beats 36.77% Runtime, 95ms
# Beats 29.37% Memory, 18.4mb