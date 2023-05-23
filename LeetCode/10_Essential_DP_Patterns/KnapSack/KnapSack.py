

class Solution:
    
    def KnapSack( self, maxCost, items ) -> int :
        
        
        dp = [ [ 0 ] * ( maxCost + 1 ) for _ in range( len( items ) + 1 ) ]
        [ print( row ) for row in dp ]
        print()
        
        for i in range( 1, len( dp ) ) :
            for j in range( 1, maxCost+1 ) :
                
                currentItemCost, currentItemVal = items[ i-1 ]
                
                valTake = dp[ i-1 ][ j-currentItemCost ] + currentItemVal if j >= currentItemCost else -1
                valSkip = dp[ i-1 ][ j ]
                
                dp[ i ][ j ] = max( valTake, valSkip )
        [ print( row ) for row in dp ]
        print()

                
        
        return dp[ -1 ][ -1 ]
    
# item = ( cost, value )
items = [ ( 4, 3 ), ( 6, 3 ), ( 2, 3 ) ]
maxCost = 12

print( f'Max Value For KnapSack: {Solution.KnapSack( super, maxCost, items ) }' )