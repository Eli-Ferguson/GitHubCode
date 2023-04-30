class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        dp = [ 0 ] * len( cost )
        dp[ 0 ] = cost[ 0 ]
        dp[ 1 ] = cost[ 1 ]

        for i in range( 2, len( cost ) ) : dp[ i ] = min( dp[ i-1 ], dp[ i-2 ] ) + cost[ i ]
        
        return min( dp[ -1 ], dp[ -2 ] )

cost = [1,100,1,1,1,100,1,1,100,1]

print( f'Min Cost of Stairs: {Solution.minCostClimbingStairs( super, cost )}' )

# Beats 54.73% Runtime, 61ms
# Beats 9.31% Memory, 16.4mb