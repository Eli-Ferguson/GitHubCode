arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

def longestIncreasingSub( arr ) :
    
    dp = [1] * len( arr ) # Initialize to the min of a problem
        
    for i in range( 1, len( arr ) ) :
                
        for j in range( 0, i ) :
            
            if arr[ i ] > arr[ j ] :
                dp[ i ] = max( dp[ i ], dp[ j ] + 1 )
            
    print( dp )
    print( max( dp ) )
    
longestIncreasingSub( arr )