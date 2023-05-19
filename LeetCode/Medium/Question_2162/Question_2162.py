class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        def cost( m, s ) :
            
            if s > 99 or m > 99 : return int( 'inf' )

            display = str( startAt ) + str( 100 * m + s )

            moves = sum( display[ i ] != display[ i-1 ] for i in range( 1, len( display ) ) )
            pushes = len( display )-1

            return moveCost * moves + pushCost * pushes

        m, s = divmod( targetSeconds, 60 )

        return min( cost( m, s ), cost( m-1, s+60 ) )

startAt = 1
moveCost = 2
pushCost = 1
targetSeconds = 600

print( f'Min Cost To Put In Numbers: {Solution.minCostSetTime( super, startAt, moveCost, pushCost, targetSeconds )}' )

# Beats 24.31% Runtime, 44ms
# Beats 11.5% Memory, 16.3mb